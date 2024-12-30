# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/cros_test_cli.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_case_result_pb2 as chromiumos_dot_test_dot_api_dot_test__case__result__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_execution_metadata_pb2 as chromiumos_dot_test_dot_api_dot_test__execution__metadata__pb2
from chromite.api.gen_sdk.chromiumos.test.api import test_suite_pb2 as chromiumos_dot_test_dot_api_dot_test__suite__pb2
from chromite.api.gen_sdk.chromiumos.test.lab.api import dut_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_dut__pb2
from chromite.api.gen_sdk.chromiumos.test.lab.api import ip_endpoint_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'chromiumos/test/api/cros_test_cli.proto\x12\x13\x63hromiumos.test.api\x1a\x19google/protobuf/any.proto\x1a*chromiumos/test/api/test_case_result.proto\x1a\x31\x63hromiumos/test/api/test_execution_metadata.proto\x1a$chromiumos/test/api/test_suite.proto\x1a!chromiumos/test/lab/api/dut.proto\x1a)chromiumos/test/lab/api/ip_endpoint.proto\"\xb7\x05\n\x0f\x43rosTestRequest\x12\x33\n\x0btest_suites\x18\x01 \x03(\x0b\x32\x1e.chromiumos.test.api.TestSuite\x12<\n\x07primary\x18\x02 \x01(\x0b\x32+.chromiumos.test.api.CrosTestRequest.Device\x12?\n\ncompanions\x18\x03 \x03(\x0b\x32+.chromiumos.test.api.CrosTestRequest.Device\x12=\n\x10inventory_server\x18\x04 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12&\n\x08metadata\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\x12&\n\x04\x61rgs\x18\x06 \x03(\x0b\x32\x18.chromiumos.test.api.Arg\x12;\n\x0fpublish_servers\x18\x07 \x03(\x0b\x32\".chromiumos.test.api.PublishServer\x1a\xa3\x02\n\x06\x44\x65vice\x12)\n\x03\x64ut\x18\x01 \x01(\x0b\x32\x1c.chromiumos.test.lab.api.Dut\x12\x37\n\ndut_server\x18\x02 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12=\n\x10provision_server\x18\x03 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12\x38\n\x0blibs_server\x18\x04 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12<\n\x0f\x64\x65vboard_server\x18\x05 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\"S\n\rPublishServer\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x34\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\"\xbb\x02\n\x10\x43rosTestResponse\x12>\n\x11test_case_results\x18\x01 \x03(\x0b\x32#.chromiumos.test.api.TestCaseResult\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12Q\n\x12given_test_results\x18\x03 \x03(\x0b\x32\x35.chromiumos.test.api.CrosTestResponse.GivenTestResult\x1al\n\x0fGivenTestResult\x12\x13\n\x0bparent_test\x18\x01 \x01(\t\x12\x44\n\x17\x63hild_test_case_results\x18\x02 \x03(\x0b\x32#.chromiumos.test.api.TestCaseResultB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.test.api.cros_test_cli_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _globals['_CROSTESTREQUEST']._serialized_start=303
  _globals['_CROSTESTREQUEST']._serialized_end=998
  _globals['_CROSTESTREQUEST_DEVICE']._serialized_start=707
  _globals['_CROSTESTREQUEST_DEVICE']._serialized_end=998
  _globals['_PUBLISHSERVER']._serialized_start=1000
  _globals['_PUBLISHSERVER']._serialized_end=1083
  _globals['_CROSTESTRESPONSE']._serialized_start=1086
  _globals['_CROSTESTRESPONSE']._serialized_end=1401
  _globals['_CROSTESTRESPONSE_GIVENTESTRESULT']._serialized_start=1293
  _globals['_CROSTESTRESPONSE_GIVENTESTRESULT']._serialized_end=1401
# @@protoc_insertion_point(module_scope)