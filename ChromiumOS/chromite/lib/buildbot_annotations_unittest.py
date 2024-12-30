# Copyright 2016 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Unittests for annotations module."""

from chromite.lib import buildbot_annotations
from chromite.lib import cros_test_lib


class TestAnnotation(cros_test_lib.TestCase):
    """Tests for Annotation."""

    def testAnnotation(self) -> None:
        steplink = buildbot_annotations.Annotation(
            "STEP_LINK", ("foo@example.com", "http://example.com/")
        )
        self.assertEqual(
            str(steplink),
            "@@@STEP_LINK@foo-AT-example.com@http://example.com/@@@",
        )

    def test_human_friendly(self) -> None:
        steplink = buildbot_annotations.Annotation(
            "STEP_LINK", ("foo@example.com", "http://example.com/")
        )
        self.assertEqual(
            steplink.human_friendly,
            "STEP_LINK: foo@example.com; http://example.com/",
        )

    def testStepText(self) -> None:
        steplink = buildbot_annotations.StepText("some text")
        self.assertEqual(str(steplink), "@@@STEP_TEXT@some text@@@")

    def testSetBuildProperty(self) -> None:
        ann = buildbot_annotations.SetBuildProperty(
            "some_property", "http://fun.com"
        )
        self.assertEqual(
            str(ann), '@@@SET_BUILD_PROPERTY@some_property@"http://fun.com"@@@'
        )

    def testSetBuildPropertyComplex(self) -> None:
        ann = buildbot_annotations.SetBuildProperty("some_property", {"a": 1})
        self.assertEqual(
            str(ann), '@@@SET_BUILD_PROPERTY@some_property@{"a": 1}@@@'
        )

    def test_human_friendly_without_args(self) -> None:
        steplink = buildbot_annotations.Annotation("STEP_FAILURE", ())
        self.assertEqual(steplink.human_friendly, "STEP_FAILURE")