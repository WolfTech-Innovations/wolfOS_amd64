# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/skylab_test_runner/cros_test_runner_service.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf.internal import builder as _builder
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import descriptor_pool as _descriptor_pool
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.test_platform import request_pb2 as test__platform_dot_request__pb2
from chromite.api.gen.chromiumos.test.lab.api import dut_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2
from chromite.api.gen.test_platform.skylab_test_runner import cft_request_pb2 as test__platform_dot_skylab__test__runner_dot_cft__request__pb2
from chromite.api.gen.test_platform.skylab_test_runner import result_pb2 as test__platform_dot_skylab__test__runner_dot_result__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?test_platform/skylab_test_runner/cros_test_runner_service.proto\x12 test_platform.skylab_test_runner\x1a\x1btest_platform/request.proto\x1a!chromiumos/test/lab/api/dut.proto\x1a\x32test_platform/skylab_test_runner/cft_request.proto\x1a-test_platform/skylab_test_runner/result.proto\"\xce\x01\n CrosTestRunnerServerStartRequest\x12\x11\n\thost_name\x18\x01 \x01(\t\x12\x18\n\x10log_data_gs_root\x18\x02 \x01(\t\x12 \n\x18\x64ocker_key_file_location\x18\x03 \x01(\t\x12:\n\x0c\x64ut_topology\x18\x04 \x01(\x0b\x32$.chromiumos.test.lab.api.DutTopology\x12\x1f\n\x17use_docker_key_directly\x18\x05 \x01(\x08\"\xdc\x01\n\x0e\x45xecuteRequest\x12\x32\n\ttest_plan\x18\x01 \x01(\x0b\x32\x1f.test_platform.Request.TestPlan\x12J\n\x10\x63\x66t_test_request\x18\x02 \x01(\x0b\x32\x30.test_platform.skylab_test_runner.CFTTestRequest\x12\x18\n\x10\x63tr_cipd_version\x18\x03 \x01(\t\x12\x18\n\x10path_to_cipd_bin\x18\x05 \x01(\t\x12\x16\n\x0e\x61rtifacts_path\x18\x04 \x01(\t\"K\n\x0f\x45xecuteResponse\x12\x38\n\x06result\x18\x01 \x01(\x0b\x32(.test_platform.skylab_test_runner.Result2\x87\x01\n\x15\x43rosTestRunnerService\x12n\n\x07\x45xecute\x12\x30.test_platform.skylab_test_runner.ExecuteRequest\x1a\x31.test_platform.skylab_test_runner.ExecuteResponseBLZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runnerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_platform.skylab_test_runner.cros_test_runner_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/skylab_test_runner'
  _CROSTESTRUNNERSERVERSTARTREQUEST._serialized_start=265
  _CROSTESTRUNNERSERVERSTARTREQUEST._serialized_end=471
  _EXECUTEREQUEST._serialized_start=474
  _EXECUTEREQUEST._serialized_end=694
  _EXECUTERESPONSE._serialized_start=696
  _EXECUTERESPONSE._serialized_end=771
  _CROSTESTRUNNERSERVICE._serialized_start=774
  _CROSTESTRUNNERSERVICE._serialized_end=909
# @@protoc_insertion_point(module_scope)