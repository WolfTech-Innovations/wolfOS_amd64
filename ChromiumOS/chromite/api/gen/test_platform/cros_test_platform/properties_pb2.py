# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test_platform/cros_test_platform/properties.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf.internal import builder as _builder
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import descriptor_pool as _descriptor_pool
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.test_platform import request_pb2 as test__platform_dot_request__pb2
from chromite.api.gen.test_platform.steps import execution_pb2 as test__platform_dot_steps_dot_execution__pb2
from chromite.api.gen.test_platform.config import config_pb2 as test__platform_dot_config_dot_config__pb2
from chromite.api.gen.chromiumos.test.api import ctp2_pb2 as chromiumos_dot_test_dot_api_dot_ctp2__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1test_platform/cros_test_platform/properties.proto\x12 test_platform.cros_test_platform\x1a\x1btest_platform/request.proto\x1a#test_platform/steps/execution.proto\x1a!test_platform/config/config.proto\x1a\x1e\x63hromiumos/test/api/ctp2.proto\"\xd6\x06\n\x1a\x43rosTestPlatformProperties\x12\'\n\x07request\x18\x02 \x01(\x0b\x32\x16.test_platform.Request\x12\\\n\x08requests\x18\x05 \x03(\x0b\x32J.test_platform.cros_test_platform.CrosTestPlatformProperties.RequestsEntry\x12,\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x1c.test_platform.config.Config\x12:\n\x08response\x18\x04 \x01(\x0b\x32$.test_platform.steps.ExecuteResponseB\x02\x18\x01\x12\x62\n\tresponses\x18\x06 \x03(\x0b\x32K.test_platform.cros_test_platform.CrosTestPlatformProperties.ResponsesEntryB\x02\x18\x01\x12\x1c\n\x14\x63ompressed_responses\x18\x08 \x01(\t\x12%\n\x19\x63ompressed_json_responses\x18\t \x01(\tB\x02\x18\x01\x12\x14\n\x0c\x66orce_export\x18\n \x01(\x08\x12\x61\n\x0b\x65xperiments\x18\x0b \x03(\x0e\x32L.test_platform.cros_test_platform.CrosTestPlatformProperties.LUCIExperiments\x12\x16\n\x0epartner_config\x18\x0c \x01(\x08\x12\x38\n\rctpv2_request\x18\r \x01(\x0b\x32!.chromiumos.test.api.CTPv2Request\x1aG\n\rRequestsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.test_platform.Request:\x02\x38\x01\x1aV\n\x0eResponsesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.test_platform.steps.ExecuteResponse:\x02\x38\x01\",\n\x0fLUCIExperiments\x12\x19\n\x15SUITE_EXECUTION_LIMIT\x10\x00J\x04\x08\x01\x10\x02\x42LZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/cros_test_platformb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'test_platform.cros_test_platform.properties_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgo.chromium.org/chromiumos/infra/proto/go/test_platform/cros_test_platform'
  _CROSTESTPLATFORMPROPERTIES_REQUESTSENTRY._options = None
  _CROSTESTPLATFORMPROPERTIES_REQUESTSENTRY._serialized_options = b'8\001'
  _CROSTESTPLATFORMPROPERTIES_RESPONSESENTRY._options = None
  _CROSTESTPLATFORMPROPERTIES_RESPONSESENTRY._serialized_options = b'8\001'
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['response']._options = None
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['response']._serialized_options = b'\030\001'
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['responses']._options = None
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['responses']._serialized_options = b'\030\001'
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['compressed_json_responses']._options = None
  _CROSTESTPLATFORMPROPERTIES.fields_by_name['compressed_json_responses']._serialized_options = b'\030\001'
  _CROSTESTPLATFORMPROPERTIES._serialized_start=221
  _CROSTESTPLATFORMPROPERTIES._serialized_end=1075
  _CROSTESTPLATFORMPROPERTIES_REQUESTSENTRY._serialized_start=864
  _CROSTESTPLATFORMPROPERTIES_REQUESTSENTRY._serialized_end=935
  _CROSTESTPLATFORMPROPERTIES_RESPONSESENTRY._serialized_start=937
  _CROSTESTPLATFORMPROPERTIES_RESPONSESENTRY._serialized_end=1023
  _CROSTESTPLATFORMPROPERTIES_LUCIEXPERIMENTS._serialized_start=1025
  _CROSTESTPLATFORMPROPERTIES_LUCIEXPERIMENTS._serialized_end=1069
# @@protoc_insertion_point(module_scope)