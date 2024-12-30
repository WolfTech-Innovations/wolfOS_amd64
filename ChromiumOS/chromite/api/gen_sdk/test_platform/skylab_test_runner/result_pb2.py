# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/result.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.test_platform.common import task_pb2 as test__platform_dot_common_dot_task__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-test_platform/skylab_test_runner/result.proto\x12 test_platform.skylab_test_runner\x1a\x1ftest_platform/common/task.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc8\x10\n\x06Result\x12L\n\x0f\x61utotest_result\x18\x01 \x01(\x0b\x32\x31.test_platform.skylab_test_runner.Result.AutotestH\x00\x12Y\n\x16\x61ndroid_generic_result\x18\x0b \x01(\x0b\x32\x37.test_platform.skylab_test_runner.Result.AndroidGenericH\x00\x12?\n\x06prejob\x18\x02 \x01(\x0b\x32/.test_platform.skylab_test_runner.Result.Prejob\x12\x33\n\x08log_data\x18\x03 \x01(\x0b\x32!.test_platform.common.TaskLogData\x12J\n\x0cstate_update\x18\x04 \x01(\x0b\x32\x34.test_platform.skylab_test_runner.Result.StateUpdate\x12W\n\x10\x61utotest_results\x18\x06 \x03(\x0b\x32=.test_platform.skylab_test_runner.Result.AutotestResultsEntry\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\thost_name\x18\t \x01(\t\x12\x45\n\rresource_urls\x18\n \x03(\x0b\x32..test_platform.skylab_test_runner.Result.Links\x12\x14\n\x0c\x65rror_string\x18\x0c \x01(\t\x12I\n\nerror_type\x18\r \x01(\x0e\x32\x35.test_platform.skylab_test_runner.TestRunnerErrorType\x1a\x81\x04\n\x08\x41utotest\x12N\n\ntest_cases\x18\x01 \x03(\x0b\x32:.test_platform.skylab_test_runner.Result.Autotest.TestCase\x12\x12\n\nincomplete\x18\x02 \x01(\x08\x1a\xf0\x02\n\x08TestCase\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x07verdict\x18\x02 \x01(\x0e\x32\x42.test_platform.skylab_test_runner.Result.Autotest.TestCase.Verdict\x12\x1e\n\x16human_readable_summary\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x82\x01\n\x07Verdict\x12\x15\n\x11VERDICT_UNDEFINED\x10\x00\x12\x10\n\x0cVERDICT_PASS\x10\x01\x12\x10\n\x0cVERDICT_FAIL\x10\x02\x12\x16\n\x12VERDICT_NO_VERDICT\x10\x03\x12\x11\n\rVERDICT_ERROR\x10\x04\x12\x11\n\rVERDICT_ABORT\x10\x05J\x04\x08\x03\x10\x04R\x18synchronous_log_data_url\x1a\x82\x02\n\x0e\x41ndroidGeneric\x12_\n\x10given_test_cases\x18\x01 \x03(\x0b\x32\x45.test_platform.skylab_test_runner.Result.AndroidGeneric.GivenTestCase\x1a\x8e\x01\n\rGivenTestCase\x12\x13\n\x0bparent_test\x18\x01 \x01(\t\x12T\n\x10\x63hild_test_cases\x18\x02 \x03(\x0b\x32:.test_platform.skylab_test_runner.Result.Autotest.TestCase\x12\x12\n\nincomplete\x18\x03 \x01(\x08\x1a\x98\x02\n\x06Prejob\x12\x42\n\x04step\x18\x01 \x03(\x0b\x32\x34.test_platform.skylab_test_runner.Result.Prejob.Step\x1a\xc9\x01\n\x04Step\x12\x0c\n\x04name\x18\x01 \x01(\t\x12M\n\x07verdict\x18\x02 \x01(\x0e\x32<.test_platform.skylab_test_runner.Result.Prejob.Step.Verdict\x12\x1e\n\x16human_readable_summary\x18\x03 \x01(\t\"D\n\x07Verdict\x12\x15\n\x11VERDICT_UNDEFINED\x10\x00\x12\x10\n\x0cVERDICT_PASS\x10\x01\x12\x10\n\x0cVERDICT_FAIL\x10\x02\x1a \n\x0bStateUpdate\x12\x11\n\tdut_state\x18\x01 \x01(\t\x1ai\n\x14\x41utotestResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.test_platform.skylab_test_runner.Result.Autotest:\x02\x38\x01\x1a\x8f\x01\n\x05Links\x12\x41\n\x04name\x18\x01 \x01(\x0e\x32\x33.test_platform.skylab_test_runner.Result.Links.Name\x12\x0b\n\x03url\x18\x02 \x01(\t\"6\n\x04Name\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tTEST_HAUS\x10\x01\x12\x12\n\x0eGOOGLE_STORAGE\x10\x02\x42\t\n\x07harnessJ\x04\x08\x05\x10\x06R\rasync_results*\x97\x01\n\x13TestRunnerErrorType\x12\x08\n\x04NONE\x10\x00\x12\x14\n\x10INPUT_VALIDATION\x10\x01\x12\x08\n\x04\x41UTH\x10\x02\x12\x12\n\x0e\x44UT_CONNECTION\x10\x03\x12\r\n\tPROVISION\x10\x04\x12\t\n\x05SERVO\x10\x05\x12\x10\n\x0cTEST_HARNESS\x10\x06\x12\x0b\n\x07PUBLISH\x10\x07\x12\t\n\x05OTHER\x10\x08\x42LZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_platform.skylab_test_runner.result_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner'
  _RESULT_AUTOTESTRESULTSENTRY._options = None
  _RESULT_AUTOTESTRESULTSENTRY._serialized_options = b'8\001'
  _globals['_TESTRUNNERERRORTYPE']._serialized_start=2273
  _globals['_TESTRUNNERERRORTYPE']._serialized_end=2424
  _globals['_RESULT']._serialized_start=150
  _globals['_RESULT']._serialized_end=2270
  _globals['_RESULT_AUTOTEST']._serialized_start=894
  _globals['_RESULT_AUTOTEST']._serialized_end=1407
  _globals['_RESULT_AUTOTEST_TESTCASE']._serialized_start=1007
  _globals['_RESULT_AUTOTEST_TESTCASE']._serialized_end=1375
  _globals['_RESULT_AUTOTEST_TESTCASE_VERDICT']._serialized_start=1245
  _globals['_RESULT_AUTOTEST_TESTCASE_VERDICT']._serialized_end=1375
  _globals['_RESULT_ANDROIDGENERIC']._serialized_start=1410
  _globals['_RESULT_ANDROIDGENERIC']._serialized_end=1668
  _globals['_RESULT_ANDROIDGENERIC_GIVENTESTCASE']._serialized_start=1526
  _globals['_RESULT_ANDROIDGENERIC_GIVENTESTCASE']._serialized_end=1668
  _globals['_RESULT_PREJOB']._serialized_start=1671
  _globals['_RESULT_PREJOB']._serialized_end=1951
  _globals['_RESULT_PREJOB_STEP']._serialized_start=1750
  _globals['_RESULT_PREJOB_STEP']._serialized_end=1951
  _globals['_RESULT_PREJOB_STEP_VERDICT']._serialized_start=1245
  _globals['_RESULT_PREJOB_STEP_VERDICT']._serialized_end=1313
  _globals['_RESULT_STATEUPDATE']._serialized_start=1953
  _globals['_RESULT_STATEUPDATE']._serialized_end=1985
  _globals['_RESULT_AUTOTESTRESULTSENTRY']._serialized_start=1987
  _globals['_RESULT_AUTOTESTRESULTSENTRY']._serialized_end=2092
  _globals['_RESULT_LINKS']._serialized_start=2095
  _globals['_RESULT_LINKS']._serialized_end=2238
  _globals['_RESULT_LINKS_NAME']._serialized_start=2184
  _globals['_RESULT_LINKS_NAME']._serialized_end=2238
# @@protoc_insertion_point(module_scope)