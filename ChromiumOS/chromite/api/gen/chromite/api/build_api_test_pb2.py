# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromite/api/build_api_test.proto
"""Generated protocol buffer code."""
from chromite.third_party.google.protobuf.internal import builder as _builder
from chromite.third_party.google.protobuf import descriptor as _descriptor
from chromite.third_party.google.protobuf import descriptor_pool as _descriptor_pool
from chromite.third_party.google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen.chromite.api import build_api_pb2 as chromite_dot_api_dot_build__api__pb2
from chromite.api.gen.chromiumos import common_pb2 as chromiumos_dot_common__pb2
from chromite.api.gen.chromiumos import metrics_pb2 as chromiumos_dot_metrics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!chromite/api/build_api_test.proto\x12\x0c\x63hromite.api\x1a\x1c\x63hromite/api/build_api.proto\x1a\x17\x63hromiumos/common.proto\x1a\x18\x63hromiumos/metrics.proto\",\n\nNestedPath\x12\x1e\n\x04path\x18\x01 \x01(\x0b\x32\x10.chromiumos.Path\"f\n\x11MultiFieldMessage\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x66lag\x18\x03 \x01(\x08\x12)\n\ttest_enum\x18\x04 \x01(\x0e\x32\x16.chromite.api.TestEnum\"\x82\x05\n\x12TestRequestMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x06\x63hroot\x18\x02 \x01(\x0b\x32\x12.chromiumos.Chroot\x12\x1e\n\x04path\x18\x03 \x01(\x0b\x32\x10.chromiumos.Path\x12&\n\x0c\x61nother_path\x18\x04 \x01(\x0b\x32\x10.chromiumos.Path\x12-\n\x0bnested_path\x18\x05 \x01(\x0b\x32\x18.chromite.api.NestedPath\x12+\n\x0bresult_path\x18\x06 \x01(\x0b\x32\x16.chromiumos.ResultPath\x12-\n\x0c\x62uild_target\x18\x07 \x01(\x0b\x32\x17.chromiumos.BuildTarget\x12.\n\rbuild_targets\x18\x08 \x03(\x0b\x32\x17.chromiumos.BuildTarget\x12)\n\nsynced_dir\x18\t \x01(\x0b\x32\x15.chromiumos.SyncedDir\x12*\n\x0bsynced_dirs\x18\n \x03(\x0b\x32\x15.chromiumos.SyncedDir\x12\x31\n\x08messages\x18\x0b \x03(\x0b\x32\x1f.chromite.api.MultiFieldMessage\x12)\n\ttest_enum\x18\x0c \x01(\x0e\x32\x16.chromite.api.TestEnum\x12*\n\ntest_enums\x18\r \x03(\x0e\x32\x16.chromite.api.TestEnum\x12\x0e\n\x06number\x18\x0e \x01(\x05\x12\x0f\n\x07numbers\x18\x0f \x03(\x05\x12\x37\n\x11remoteexec_config\x18\x10 \x01(\x0b\x32\x1c.chromiumos.RemoteexecConfig\"\xc8\x01\n\x11TestResultMessage\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\"\n\x08\x61rtifact\x18\x02 \x01(\x0b\x32\x10.chromiumos.Path\x12\x31\n\x0fnested_artifact\x18\x03 \x01(\x0b\x32\x18.chromite.api.NestedPath\x12#\n\tartifacts\x18\x04 \x03(\x0b\x32\x10.chromiumos.Path\x12\'\n\x06\x65vents\x18\x05 \x03(\x0b\x32\x17.chromiumos.MetricEvent*^\n\x08TestEnum\x12\x19\n\x15TEST_ENUM_UNSPECIFIED\x10\x00\x12\x11\n\rTEST_ENUM_FOO\x10\x01\x12\x11\n\rTEST_ENUM_BAR\x10\x02\x12\x11\n\rTEST_ENUM_BAZ\x10\x03\x32\xc0\x02\n\x0eTestApiService\x12V\n\x11InputOutputMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12\x65\n\rRenamedMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x11\xc2\xed\x1a\r\n\x0b\x43orrectName\x12Y\n\x0cHiddenMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x18\x02\x1a\x14\xc2\xed\x1a\x10\n\x0e\x62uild_api_test2\xf9\x01\n\x16InsideChrootApiService\x12^\n\x19InsideServiceInsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12g\n\x1aInsideServiceOutsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x10\x02\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x01\x32\xfc\x01\n\x17OutsideChrootApiService\x12`\n\x1bOutsideServiceOutsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12g\n\x1aOutsideServiceInsideMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x10\x01\x1a\x16\xc2\xed\x1a\x12\n\x0e\x62uild_api_test\x10\x02\x32|\n\rHiddenService\x12Q\n\x0cHiddenMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x1a\x18\xc2\xed\x1a\x14\n\x0e\x62uild_api_test\x10\x02\x18\x02\x32\xc5\x03\n\x13TotExecutionService\x12X\n\x13TotServiceTotMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\x12\x66\n\x19TotServiceTotMethodInside\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02\x10\x01\x12\x65\n\x18TotServiceBranchedMethod\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02 \x01\x12k\n\x1eTotServiceBranchedMethodInside\x12 .chromite.api.TestRequestMessage\x1a\x1f.chromite.api.TestResultMessage\"\x06\xc2\xed\x1a\x02 \x01\x1a\x18\xc2\xed\x1a\x14\n\x0e\x62uild_api_test\x10\x02 \x02\x42\x38Z6go.chromium.org/chromiumos/infra/proto/go/chromite/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromite.api.build_api_test_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6go.chromium.org/chromiumos/infra/proto/go/chromite/api'
  _TESTAPISERVICE._options = None
  _TESTAPISERVICE._serialized_options = b'\302\355\032\020\n\016build_api_test'
  _TESTAPISERVICE.methods_by_name['RenamedMethod']._options = None
  _TESTAPISERVICE.methods_by_name['RenamedMethod']._serialized_options = b'\302\355\032\r\n\013CorrectName'
  _TESTAPISERVICE.methods_by_name['HiddenMethod']._options = None
  _TESTAPISERVICE.methods_by_name['HiddenMethod']._serialized_options = b'\302\355\032\002\030\002'
  _INSIDECHROOTAPISERVICE._options = None
  _INSIDECHROOTAPISERVICE._serialized_options = b'\302\355\032\022\n\016build_api_test\020\001'
  _INSIDECHROOTAPISERVICE.methods_by_name['InsideServiceOutsideMethod']._options = None
  _INSIDECHROOTAPISERVICE.methods_by_name['InsideServiceOutsideMethod']._serialized_options = b'\302\355\032\002\020\002'
  _OUTSIDECHROOTAPISERVICE._options = None
  _OUTSIDECHROOTAPISERVICE._serialized_options = b'\302\355\032\022\n\016build_api_test\020\002'
  _OUTSIDECHROOTAPISERVICE.methods_by_name['OutsideServiceInsideMethod']._options = None
  _OUTSIDECHROOTAPISERVICE.methods_by_name['OutsideServiceInsideMethod']._serialized_options = b'\302\355\032\002\020\001'
  _HIDDENSERVICE._options = None
  _HIDDENSERVICE._serialized_options = b'\302\355\032\024\n\016build_api_test\020\002\030\002'
  _TOTEXECUTIONSERVICE._options = None
  _TOTEXECUTIONSERVICE._serialized_options = b'\302\355\032\024\n\016build_api_test\020\002 \002'
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceTotMethodInside']._options = None
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceTotMethodInside']._serialized_options = b'\302\355\032\002\020\001'
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceBranchedMethod']._options = None
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceBranchedMethod']._serialized_options = b'\302\355\032\002 \001'
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceBranchedMethodInside']._options = None
  _TOTEXECUTIONSERVICE.methods_by_name['TotServiceBranchedMethodInside']._serialized_options = b'\302\355\032\002 \001'
  _TESTENUM._serialized_start=1130
  _TESTENUM._serialized_end=1224
  _NESTEDPATH._serialized_start=132
  _NESTEDPATH._serialized_end=176
  _MULTIFIELDMESSAGE._serialized_start=178
  _MULTIFIELDMESSAGE._serialized_end=280
  _TESTREQUESTMESSAGE._serialized_start=283
  _TESTREQUESTMESSAGE._serialized_end=925
  _TESTRESULTMESSAGE._serialized_start=928
  _TESTRESULTMESSAGE._serialized_end=1128
  _TESTAPISERVICE._serialized_start=1227
  _TESTAPISERVICE._serialized_end=1547
  _INSIDECHROOTAPISERVICE._serialized_start=1550
  _INSIDECHROOTAPISERVICE._serialized_end=1799
  _OUTSIDECHROOTAPISERVICE._serialized_start=1802
  _OUTSIDECHROOTAPISERVICE._serialized_end=2054
  _HIDDENSERVICE._serialized_start=2056
  _HIDDENSERVICE._serialized_end=2180
  _TOTEXECUTIONSERVICE._serialized_start=2183
  _TOTEXECUTIONSERVICE._serialized_end=2636
# @@protoc_insertion_point(module_scope)