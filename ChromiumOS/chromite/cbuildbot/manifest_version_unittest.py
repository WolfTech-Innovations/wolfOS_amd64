# Copyright 2012 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for manifest_version. Needs to be run inside of chroot."""

import os
from unittest import mock

from chromite.cbuildbot import build_status
from chromite.cbuildbot import manifest_version
from chromite.cbuildbot import repository
from chromite.lib import builder_status_lib
from chromite.lib import chromeos_version
from chromite.lib import cros_test_lib
from chromite.lib import git
from chromite.lib import osutils
from chromite.lib import timeout_util
from chromite.lib.buildstore import BuildIdentifier
from chromite.lib.buildstore import FakeBuildStore
from chromite.lib.chromeos_version_unittest import VersionInfoTest


FAKE_VERSION = """
CHROMEOS_BUILD=%(build_number)s
CHROMEOS_BRANCH=%(branch_build_number)s
CHROMEOS_PATCH=%(patch_number)s
CHROME_BRANCH=%(chrome_branch)s
"""

FAKE_WHITELISTED_REMOTES = ("cros", "chromium")
FAKE_NON_WHITELISTED_REMOTE = "hottubtimemachine"

FAKE_VERSION_STRING = "1.2.3"
FAKE_VERSION_STRING_NEXT = "1.2.4"
CHROME_BRANCH = "13"

# Use the chromite repo to actually test git changes.
GIT_TEST_PATH = "chromite"

MOCK_BUILD_ID = 162345


# pylint: disable=protected-access


class HelperMethodsTest(cros_test_lib.TempDirTestCase):
    """Test methods associated with methods not in a class."""

    def testCreateSymlink(self) -> None:
        """Tests that we can create symlinks and remove a previous one."""
        srcfile = os.path.join(self.tempdir, "src")
        osutils.Touch(srcfile)
        other_dir = os.path.join(self.tempdir, "other_dir")
        os.makedirs(other_dir)
        destfile = os.path.join(other_dir, "dest")

        manifest_version.CreateSymlink(srcfile, destfile)
        self.assertTrue(
            os.path.lexists(destfile),
            "Unable to create symlink to %s" % destfile,
        )


class ResolveHelpersTest(cros_test_lib.TempDirTestCase):
    """Test the buildspec resolution helper functions."""

    def setUp(self) -> None:
        self.mv_path = self.tempdir

        self.version = "1.2.3"
        self.resolvedVersionSpec = os.path.join(
            self.mv_path, "buildspecs", "12", "1.2.3.xml"
        )

        self.invalidSpec = os.path.join("invalid", "spec")

        self.validSpec = os.path.join("valid", "spec")
        self.resolvedValidSpec = os.path.join(self.mv_path, "valid", "spec.xml")

        osutils.Touch(self.resolvedVersionSpec, makedirs=True)
        osutils.Touch(self.resolvedValidSpec, makedirs=True)

    def testResolveBuildspec(self) -> None:
        """Test ResolveBuildspec."""
        result = manifest_version.ResolveBuildspec(self.mv_path, self.validSpec)
        self.assertEqual(result, self.resolvedValidSpec)

        result = manifest_version.ResolveBuildspec(
            self.mv_path, self.validSpec + ".xml"
        )
        self.assertEqual(result, self.resolvedValidSpec)

        with self.assertRaises(manifest_version.BuildSpecsValueError):
            manifest_version.ResolveBuildspec(self.mv_path, self.invalidSpec)

    def testResolveBuildspecVersion(self) -> None:
        """Test ResolveBuildspecVersion."""
        result = manifest_version.ResolveBuildspecVersion(
            self.mv_path, self.version
        )
        self.assertEqual(result, self.resolvedVersionSpec)

        with self.assertRaises(manifest_version.BuildSpecsValueError):
            manifest_version.ResolveBuildspecVersion(self.mv_path, "1.2.0")


class FilterManifestTest(cros_test_lib.TempDirTestCase):
    """Test for FilterManifest."""

    def testSimple(self) -> None:
        """Basic check of functionality."""
        path = os.path.join(self.tempdir, "input.xml")
        osutils.WriteFile(
            path,
            """\
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <include name="default.xml" />
</manifest>
""",
        )
        new_path = manifest_version.FilterManifest(path)
        self.assertEqual(
            """\
<?xml version="1.0" encoding="utf-8"?><manifest>
<include name="default.xml"/>
</manifest>\
""",
            osutils.ReadFile(new_path),
        )


class BuildSpecFunctionsTest(cros_test_lib.MockTempDirTestCase):
    """Tests for methods related to publishing buildspecs."""

    def setUp(self) -> None:
        self.version_info = chromeos_version.VersionInfo("1.2.3", "11")

        self.manifest_versions_int = os.path.join(
            self.tempdir, "manifest_versions_int"
        )
        self.manifest_versions_ext = os.path.join(
            self.tempdir, "manifest_versions_ext"
        )

    def testOfficialBuildSpecPath(self) -> None:
        """Test OfficialBuildSpecPath."""
        result = manifest_version.OfficialBuildSpecPath(self.version_info)
        self.assertEqual(result, "buildspecs/11/1.2.3.xml")

    def testPopulateAndPublishBuildSpec(self) -> None:
        """Test PopulateAndPublishBuildSpec."""
        commitMock = self.PatchObject(manifest_version, "_CommitAndPush")

        filter_out = os.path.join(self.tempdir, "filter_out")
        osutils.WriteFile(filter_out, "filtered mani")
        self.PatchObject(
            manifest_version, "FilterManifest", return_value=filter_out
        )

        manifest_version.PopulateAndPublishBuildSpec(
            "spec",
            "int mani",
            self.manifest_versions_int,
            self.manifest_versions_ext,
            dryrun=True,
        )

        self.assertEqual(
            commitMock.call_args_list,
            [
                mock.call(
                    self.manifest_versions_int,
                    "https://chrome-internal.googlesource.com/chromeos/"
                    "manifest-versions",
                    "spec",
                    "int mani",
                    True,
                ),
                mock.call(
                    self.manifest_versions_ext,
                    "https://chromium.googlesource.com/chromiumos/"
                    "manifest-versions",
                    "spec",
                    "filtered mani",
                    True,
                ),
            ],
        )

    def testPopulateAndPublishBuildSpecIntOnly(self) -> None:
        """Test PopulateAndPublishBuildSpec (no external manifest versions)."""
        commitMock = self.PatchObject(manifest_version, "_CommitAndPush")

        filter_out = os.path.join(self.tempdir, "filter_out")
        osutils.WriteFile(filter_out, "filtered mani")
        self.PatchObject(
            manifest_version, "FilterManifest", return_value=filter_out
        )

        manifest_version.PopulateAndPublishBuildSpec(
            "spec", "int mani", self.manifest_versions_int, None, dryrun=False
        )

        self.assertEqual(
            commitMock.call_args_list,
            [
                mock.call(
                    self.manifest_versions_int,
                    "https://chrome-internal.googlesource.com/chromeos/"
                    "manifest-versions",
                    "spec",
                    "int mani",
                    False,
                ),
            ],
        )


class BuildSpecsManagerTest(cros_test_lib.MockTempDirTestCase):
    """Tests for the BuildSpecs manager."""

    def setUp(self) -> None:
        os.makedirs(os.path.join(self.tempdir, ".repo"))
        self.source_repo = "ssh://source/repo"
        self.manifest_repo = "ssh://manifest/repo"
        self.version_file = "version-file.sh"
        self.branch = "master"
        self.build_names = ["amd64-generic-release"]
        self.incr_type = "branch"
        # Change default to something we clean up.
        self.tmpmandir = os.path.join(self.tempdir, "man")
        osutils.SafeMakedirs(self.tmpmandir)
        self.manager = None

        self.PatchObject(
            builder_status_lib.SlaveBuilderStatus, "_InitSlaveInfo"
        )

        self.db = mock.Mock()
        self.buildstore = FakeBuildStore(self.db)
        self.buildbucket_client_mock = mock.Mock()

    def BuildManager(self, config=None, metadata=None, buildbucket_client=None):
        repo = repository.RepoRepository(
            self.source_repo, self.tempdir, self.branch
        )
        manager = manifest_version.BuildSpecsManager(
            repo,
            self.manifest_repo,
            self.build_names,
            self.incr_type,
            False,
            branch=self.branch,
            dry_run=True,
            config=config,
            metadata=metadata,
            buildstore=self.buildstore,
            buildbucket_client=buildbucket_client,
        )
        manager.manifest_dir = self.tmpmandir
        # Shorten the sleep between attempts.
        manager.SLEEP_TIMEOUT = 1

        return manager

    def testPublishManifestCommitMessageWithBuildId(self) -> None:
        """Tests that PublishManifest writes a build id."""
        self.manager = self.BuildManager()
        expected_message = (
            "Automatic: Start amd64-generic-release master 1\nCrOS-Build-Id: %s"
            % MOCK_BUILD_ID
        )
        push_mock = self.PatchObject(self.manager, "PushSpecChanges")

        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )

        # Create a fake manifest file.
        m = os.path.join(self.tmpmandir, "1.xml")
        osutils.Touch(m)
        self.manager.InitializeManifestVariables(info)

        self.manager.PublishManifest(m, "1", build_id=MOCK_BUILD_ID)

        push_mock.assert_called_once_with(expected_message)

    def testPublishManifestCommitMessageWithNegativeBuildId(self) -> None:
        """Tests that PublishManifest doesn't write a negative build_id"""
        self.manager = self.BuildManager()
        expected_message = "Automatic: Start amd64-generic-release master 1"
        push_mock = self.PatchObject(self.manager, "PushSpecChanges")

        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )

        # Create a fake manifest file.
        m = os.path.join(self.tmpmandir, "1.xml")
        osutils.Touch(m)
        self.manager.InitializeManifestVariables(info)

        self.manager.PublishManifest(m, "1", build_id=-1)

        push_mock.assert_called_once_with(expected_message)

    def testPublishManifestCommitMessageWithNoneBuildId(self) -> None:
        """Tests that PublishManifest doesn't write a non-existant build_id"""
        self.manager = self.BuildManager()
        expected_message = "Automatic: Start amd64-generic-release master 1"
        push_mock = self.PatchObject(self.manager, "PushSpecChanges")

        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )

        # Create a fake manifest file.
        m = os.path.join(self.tmpmandir, "1.xml")
        osutils.Touch(m)
        self.manager.InitializeManifestVariables(info)

        self.manager.PublishManifest(m, "1")

        push_mock.assert_called_once_with(expected_message)

    def _buildManifest(self):
        mpath = os.path.join(
            self.manager.manifest_dir, "buildspecs", CHROME_BRANCH
        )
        manifest_paths = [
            os.path.join(mpath, "1.2.%d.xml" % x) for x in [2, 3, 4, 5]
        ]
        # Create fake buildspecs.
        osutils.SafeMakedirs(os.path.join(mpath))
        for m in manifest_paths:
            osutils.Touch(m)

        return manifest_paths

    def testInitializeManifestVariablesWithUnprocessedBuild(self) -> None:
        """Test InitializeManifestVariables with unprocessed build."""
        self.manager = self.BuildManager()
        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )
        for_build = os.path.join(
            self.manager.manifest_dir, "build-name", self.build_names[0]
        )

        m1, m2, _, _ = self._buildManifest()
        # Fail 1, pass 2, leave 3,4 unprocessed.
        manifest_version.CreateSymlink(
            m1,
            os.path.join(
                for_build, "fail", CHROME_BRANCH, os.path.basename(m1)
            ),
        )
        manifest_version.CreateSymlink(
            m1,
            os.path.join(
                for_build, "pass", CHROME_BRANCH, os.path.basename(m2)
            ),
        )

        self.manager.buildstore.fake_cidb.GetBuildHistory.return_value = None
        self.manager.InitializeManifestVariables(info)
        self.assertEqual(self.manager.latest_unprocessed, "1.2.5")
        self.assertIsNone(self.manager._latest_build)

    def testInitializeManifestVariablesWithPassedBuild(self) -> None:
        """Test InitializeManifestVariables with passed build."""
        self.manager = self.BuildManager()
        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )
        for_build = os.path.join(
            self.manager.manifest_dir, "build-name", self.build_names[0]
        )

        m1, m2, m3, m4 = self._buildManifest()
        # Fail 1, pass 2, pass 3, pass 4
        manifest_version.CreateSymlink(
            m1,
            os.path.join(
                for_build, "fail", CHROME_BRANCH, os.path.basename(m1)
            ),
        )
        for m in [m2, m3, m4]:
            manifest_version.CreateSymlink(
                m,
                os.path.join(
                    for_build, "pass", CHROME_BRANCH, os.path.basename(m)
                ),
            )

        latest_builds = [
            {
                "build_config": self.build_names[0],
                "status": "pass",
                "platform_version": "1.2.5",
            }
        ]
        self.manager.buildstore.fake_cidb.GetBuildHistory.return_value = (
            latest_builds
        )
        self.manager.InitializeManifestVariables(info)
        self.assertIsNone(self.manager.latest_unprocessed)
        self.assertEqual(self.manager._latest_build, latest_builds[0])

    def testLatestSpecFromDir(self) -> None:
        """Tests whether we can get sorted specs correctly from a directory."""
        self.manager = self.BuildManager()
        self.PatchObject(git, "Clone", side_effect=Exception())
        info = chromeos_version.VersionInfo(
            "99.1.2", CHROME_BRANCH, incr_type="branch"
        )

        specs_dir = os.path.join(
            self.manager.manifest_dir, "buildspecs", CHROME_BRANCH
        )
        m1, m2, m3, m4 = [
            os.path.join(specs_dir, x)
            for x in ["100.0.0.xml", "99.3.3.xml", "99.1.10.xml", "99.1.5.xml"]
        ]

        # Create fake buildspecs.
        osutils.SafeMakedirs(specs_dir)
        for m in [m1, m2, m3, m4]:
            osutils.Touch(m)

        spec = self.manager._LatestSpecFromDir(info, specs_dir)
        # Should be the latest on the 99.1 branch.
        self.assertEqual(spec, "99.1.10")

    def testGetNextVersionNoIncrement(self) -> None:
        """Tests whether we can get the next version to be built correctly.

        Tests without pre-existing version in manifest dir.
        """
        self.manager = self.BuildManager()
        info = chromeos_version.VersionInfo(
            FAKE_VERSION_STRING, CHROME_BRANCH, incr_type="branch"
        )

        self.manager.latest = None
        version = self.manager.GetNextVersion(info)
        self.assertEqual(FAKE_VERSION_STRING, version)

    def testGetNextVersionIncrement(self) -> None:
        """Tests that we create a new version if a previous one exists."""
        self.manager = self.BuildManager()
        self.manager.dry_run = False
        m = self.PatchObject(chromeos_version.VersionInfo, "UpdateVersionFile")
        version_file = VersionInfoTest.CreateFakeVersionFile(self.tempdir)
        info = chromeos_version.VersionInfo(
            version_file=version_file, incr_type="branch"
        )

        self.manager.latest = FAKE_VERSION_STRING
        version = self.manager.GetNextVersion(info)
        self.assertEqual(FAKE_VERSION_STRING_NEXT, version)
        m.assert_called_once_with(
            "Automatic: %s - Updating to a new version number from %s"
            % (self.build_names[0], FAKE_VERSION_STRING),
            dry_run=False,
        )

    def testGetNextVersionDryRun(self) -> None:
        """Tests that we reuse a previous version if it is a dryrun."""
        self.manager = self.BuildManager()
        m = self.PatchObject(chromeos_version.VersionInfo, "UpdateVersionFile")
        version_file = VersionInfoTest.CreateFakeVersionFile(self.tempdir)
        info = chromeos_version.VersionInfo(
            version_file=version_file, incr_type="branch"
        )

        self.manager.latest = FAKE_VERSION_STRING
        version = self.manager.GetNextVersion(info)
        self.assertEqual(FAKE_VERSION_STRING, version)
        m.assert_called_once_with(
            "Automatic: %s - Updating to a new version number from %s"
            % (self.build_names[0], FAKE_VERSION_STRING),
            dry_run=True,
        )

    def testGetNextBuildSpec(self) -> None:
        """End-to-end test of updating the manifest."""
        self.manager = self.BuildManager()
        my_info = chromeos_version.VersionInfo("1.2.3", chrome_branch="4")
        self.PatchObject(
            manifest_version.BuildSpecsManager,
            "GetCurrentVersionInfo",
            return_value=my_info,
        )
        self.PatchObject(repository.RepoRepository, "Sync")
        self.PatchObject(
            repository.RepoRepository,
            "ExportManifest",
            return_value="<manifest />",
        )
        rc = self.StartPatcher(cros_test_lib.RunCommandMock())
        rc.SetDefaultCmdResult()

        self.manager.GetNextBuildSpec(retries=0)
        self.manager.UpdateStatus({self.build_names[0]: True})

    def testDidLastBuildFailReturnsFalse(self) -> None:
        """Test DidLastBuildFail returns False."""
        self.manager = self.BuildManager()
        self.assertFalse(self.manager.DidLastBuildFail())

    # pylint: disable=attribute-defined-outside-init
    def testDidLastBuildFailReturnsTrue(self) -> None:
        """Test DidLastBuildFailReturns True."""
        self.manager = self.BuildManager()
        self._latest_build = {
            "build_config": self.build_names[0],
            "status": "fail",
            "platform_version": "1.2.5",
        }
        self.assertFalse(self.manager.DidLastBuildFail())

    def testWaitForSlavesToCompleteWithEmptyBuildersArray(self) -> None:
        """Test WaitForSlavesToComplete with an empty builders_array."""
        self.manager = self.BuildManager()
        self.manager.WaitForSlavesToComplete(1, [])

    def testWaitForSlavesToComplete(self) -> None:
        """Test WaitForSlavesToComplete."""
        self.PatchObject(build_status.SlaveStatus, "UpdateSlaveStatus")
        self.PatchObject(
            build_status.SlaveStatus, "ShouldWait", return_value=False
        )
        self.manager = self.BuildManager()
        self.manager.WaitForSlavesToComplete(
            BuildIdentifier(cidb_id=1, buildbucket_id=1234),
            ["build_1", "build_2"],
        )

    def testWaitForSlavesToCompleteWithTimeout(self) -> None:
        """Test WaitForSlavesToComplete raises timeout."""
        self.PatchObject(build_status.SlaveStatus, "UpdateSlaveStatus")
        self.PatchObject(
            build_status.SlaveStatus, "ShouldWait", return_value=True
        )
        self.manager = self.BuildManager()
        self.assertRaises(
            timeout_util.TimeoutError,
            self.manager.WaitForSlavesToComplete,
            BuildIdentifier(cidb_id=1, buildbucket_id=1234),
            ["build_1", "build_2"],
            timeout=1,
            ignore_timeout_exception=False,
        )