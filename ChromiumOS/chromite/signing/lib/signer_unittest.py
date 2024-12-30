# Copyright 2018 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittest ChromeOS image signer logic"""

import configparser
import io
import os

from chromite.lib import cros_test_lib
from chromite.signing.lib import keys
from chromite.signing.lib import keys_unittest
from chromite.signing.lib import signer


class TestSignerConfig(cros_test_lib.TestCase):
    """Test SignerConfig."""

    def GetSignerConfig(
        self,
        archive="foo.tar.bz2",
        board="link",
        artifact_type="update_payload",
        version="1.2.3.4",
        versionrev="R24-1.2.3.4",
        keyset="link-mp",
        channel="dev",
        input_files=("foo.bin"),
        output_files=("@ROOTNAME@-@VERSION@.bin"),
    ):
        """Returns SignerConfig, providing the defaults."""
        return signer.SignerInstructionConfig(
            archive=archive,
            board=board,
            artifact_type=artifact_type,
            version=version,
            versionrev=versionrev,
            keyset=keyset,
            channel=channel,
            input_files=input_files,
            output_files=output_files,
        )

    def testToIniDictSimple(self) -> None:
        self.assertDictEqual(
            self.GetSignerConfig().ToIniDict(),
            {
                "general": {
                    "archive": "foo.tar.bz2",
                    "board": "link",
                    "type": "update_payload",
                    "version": "1.2.3.4",
                    "versionrev": "R24-1.2.3.4",
                },
                "insns": {
                    "keyset": "link-mp",
                    "channel": "dev",
                    "input_files": "foo.bin",
                    "output_names": "@ROOTNAME@-@VERSION@.bin",
                },
            },
        )

    def testReadIniFile(self) -> None:
        initial_sc = self.GetSignerConfig()

        # Create INI file from initial SignerConfig
        cp = configparser.ConfigParser()
        for section, options in initial_sc.ToIniDict().items():
            cp.add_section(section)
            for option, value in options.items():
                cp.set(section, option, value=value)
        ini_in_file = io.StringIO()
        cp.write(ini_in_file)

        # Read INI to new SignerConfig
        read_sc = signer.SignerInstructionConfig()
        ini_in_file.seek(0)
        read_sc.ReadIniFile(ini_in_file)

        self.assertEqual(initial_sc, read_sc)

    def testGetFilePairsSimple(self) -> None:
        in_files = "foo.bar"
        out_files = "foo.out.bar"
        sc = self.GetSignerConfig(input_files=in_files, output_files=out_files)
        self.assertListEqual(sc.GetFilePairs(), [(in_files, out_files)])

    def testGetFilePairsSimpleMultiple(self) -> None:
        in_files = ("foo.bin", "bar.bin")
        out_files = ("foo.out.bin", "bar.out.bin")
        sc = self.GetSignerConfig(input_files=in_files, output_files=out_files)
        self.assertListEqual(
            sc.GetFilePairs(),
            [("foo.bin", "foo.out.bin"), ("bar.bin", "bar.out.bin")],
        )

    def testGetFilePairsSimpleTemplate(self) -> None:
        in_files = "foo.bar"
        sc = self.GetSignerConfig(input_files=in_files)
        self.assertListEqual(sc.GetFilePairs(), [(in_files, "foo-1.2.3.4.bin")])

    def testGetFilePairsDefault(self) -> None:
        in_file = "foo.bar"
        out_file = (
            "chromeos_1.2.3.4_link_update_payload_dev-channel_link-mp.bin"
        )
        sc = self.GetSignerConfig(input_files=in_file, output_files=())
        self.assertListEqual(sc.GetFilePairs(), [(in_file, out_file)])

    def testGetFilePairsMultipleInput(self) -> None:
        in_files = ("foo.bin", "bar.bin")
        sc = self.GetSignerConfig(input_files=in_files)
        self.assertListEqual(
            sc.GetFilePairs(),
            [("foo.bin", "foo-1.2.3.4.bin"), ("bar.bin", "bar-1.2.3.4.bin")],
        )

    def testGetFilePairsMultipleInputDefaultTemp(self) -> None:
        in_files = ("foo.bin", "bar.bin")
        sc = self.GetSignerConfig(input_files=in_files, output_files=())
        with self.assertRaises(signer.SignerOutputTemplateError):
            sc.GetFilePairs()

    def testFillTemplate(self) -> None:
        sc = self.GetSignerConfig()

        in_file = "/tmp/foo.bar"
        self.assertEqual("foo.out", sc.FillTemplate("foo.out"))
        self.assertEqual(
            "foo.out", sc.FillTemplate("foo.out", filename=in_file)
        )

        self.assertEqual("__link__", sc.FillTemplate("__@BOARD@__"))
        self.assertEqual("__dev__", sc.FillTemplate("__@CHANNEL@__"))
        self.assertEqual("__link-mp__", sc.FillTemplate("__@KEYSET@__"))
        self.assertEqual("__update_payload__", sc.FillTemplate("__@TYPE@__"))
        self.assertEqual("__1.2.3.4__", sc.FillTemplate("__@VERSION@__"))

        self.assertEqual(
            "__foo.bar__", sc.FillTemplate("__@BASENAME@__", filename=in_file)
        )

        self.assertEqual(
            "__foo__", sc.FillTemplate("__@ROOTNAME@__", filename=in_file)
        )


class MockBaseSigner(signer.BaseSigner):
    """Configurable Signer for testing."""

    def __init__(
        self,
        required_keys=None,
        required_keys_public=None,
        required_keys_private=None,
        required_keyblocks=None,
    ) -> None:
        """Create a Signer based on the passed required lists."""
        self.required_keys = required_keys or []
        self.required_keys_public = required_keys_public or []
        self.required_keys_private = required_keys_private or []
        self.required_keyblocks = required_keyblocks or []

    def Sign(self, keyset, input_name, output_name):
        """Always return True on signing."""
        return True


class TestSigner(cros_test_lib.TempDirTestCase):
    """Test Signer."""

    def testSign(self) -> None:
        ks = keys.Keyset()
        s = signer.BaseSigner()
        with self.assertRaises(NotImplementedError):
            s.Sign(ks, "input", "output")

    def testCheck(self) -> None:
        ks = keys.Keyset()
        s = signer.BaseSigner()
        self.assertTrue(s.CheckKeyset(ks))

    def testCheckRequiredKeysMissing(self) -> None:
        ks_empty = keys.Keyset()
        s0 = MockBaseSigner(required_keys=["key1"])
        self.assertFalse(s0.CheckKeyset(ks_empty))

    def testCheckRequiredKeys(self) -> None:
        s0 = MockBaseSigner(required_keys=["key1"])
        ks0 = KeysetFromSigner(s0, self.tempdir)
        self.assertTrue(s0.CheckKeyset(ks0))

    def testCheckRequiredPublicKeysMissing(self) -> None:
        ks_empty = keys.Keyset()
        s0 = MockBaseSigner(required_keys_public=["key1"])
        self.assertFalse(s0.CheckKeyset(ks_empty))

    def testCheckRequiredPublicKeys(self) -> None:
        s0 = MockBaseSigner(required_keys_public=["key1"])
        ks0 = KeysetFromSigner(s0, self.tempdir)
        self.assertTrue(s0.CheckKeyset(ks0))

    def testCheckRequiredPrivateKeysMissing(self) -> None:
        ks_empty = keys.Keyset()
        s0 = MockBaseSigner(required_keys_private=["key1"])
        self.assertFalse(s0.CheckKeyset(ks_empty))

    def testCheckRequiredPrivateKeys(self) -> None:
        s0 = MockBaseSigner(required_keys_private=["key1"])
        ks0 = KeysetFromSigner(s0, self.tempdir)
        self.assertTrue(s0.CheckKeyset(ks0))

    def testCheckRequiredKeyblocksEmpty(self) -> None:
        ks_empty = keys.Keyset()
        s0 = MockBaseSigner(required_keyblocks=["key1"])
        self.assertFalse(s0.CheckKeyset(ks_empty))

    def testCheckRequiredKeyblocks(self) -> None:
        s0 = MockBaseSigner(required_keyblocks=["key1"])
        ks0 = KeysetFromSigner(s0, self.tempdir)
        self.assertTrue(s0.CheckKeyset(ks0))


def KeysetFromSigner(s, keydir, subdir="keyset"):
    """Returns a valid keyset containing required keys and keyblocks."""
    ks = keys.Keyset()

    keydir = os.path.join(keydir, subdir)

    for key_name in s.required_keys:
        key = keys.KeyPair(key_name, keydir=keydir)
        ks.AddKey(key)
        keys_unittest.CreateStubKeys(key)

    for key_name in s.required_keys_public:
        key = keys.KeyPair(key_name, keydir=keydir)
        ks.AddKey(key)
        keys_unittest.CreateStubPublic(key)

        if key in s.required_keyblocks:
            keys_unittest.CreateStubKeyblock(key)

    for key_name in s.required_keys_private:
        key = keys.KeyPair(key_name, keydir=keydir)
        ks.AddKey(key)
        keys_unittest.CreateStubPrivateKey(key)

    for keyblock_name in s.required_keyblocks:
        if keyblock_name not in ks.keys:
            ks.AddKey(keys.KeyPair(keyblock_name, keydir=keydir))

        key = ks.keys[keyblock_name]
        keys_unittest.CreateStubKeyblock(key)

    return ks


class MockFutilitySigner(signer.FutilitySigner):
    """Basic implementation of a FutilitySigner."""

    required_keys = ("foo",)

    def GetFutilityArgs(self, keyset, input_name, output_name):
        """Returns a list of [input_name, output_name]."""
        return [input_name, output_name]


class TestFutilitySigner(cros_test_lib.RunCommandTempDirTestCase):
    """Test Futility Signer."""

    def testSign(self) -> None:
        keyset = keys.Keyset()
        fs = signer.FutilitySigner()
        self.assertRaises(NotImplementedError, fs.Sign, keyset, "stub", "stub")

    def testSignWithMock(self) -> None:
        foo_key = keys.KeyPair("foo", self.tempdir)
        keys_unittest.CreateStubKeys(foo_key)

        keyset = keys.Keyset()
        keyset.AddKey(foo_key)

        fsm = MockFutilitySigner()
        fsm.Sign(keyset, "foo", "bar")
        self.assertCommandContains(["foo", "bar"])

    def testSignWithMockMissingKey(self) -> None:
        keyset = keys.Keyset()
        fsm = MockFutilitySigner()
        self.assertFalse(fsm.Sign(keyset, "foo", "bar"))

    def testGetCmdArgs(self) -> None:
        keyset = keys.Keyset()
        fs = signer.FutilitySigner()
        self.assertRaises(
            NotImplementedError, fs.GetFutilityArgs, keyset, "foo", "bar"
        )


class TestFutilityFunction(cros_test_lib.RunCommandTestCase):
    """Test Futility command."""

    def testCommand(self) -> None:
        self.assertTrue(
            signer.RunFutility([]), msg="Futility should pass w/ mock"
        )
        self.assertCommandContains(["futility"])

    def testCommandWithArgs(self) -> None:
        args = ["--privkey", "foo.priv2"]
        signer.RunFutility(args)
        self.assertCommandContains(args)