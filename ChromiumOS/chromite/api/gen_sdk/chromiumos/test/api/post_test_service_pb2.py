# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chromiumos/test/api/post_test_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chromite.api.gen_sdk.chromiumos.test.lab.api import ip_endpoint_pb2 as chromiumos_dot_test_dot_lab_dot_api_dot_ip__endpoint__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+chromiumos/test/api/post_test_service.proto\x12\x13\x63hromiumos.test.api\x1a)chromiumos/test/lab/api/ip_endpoint.proto\x1a\x19google/protobuf/any.proto\"y\n\x16PostTestStartUpRequest\x12\x37\n\ndut_server\x18\x01 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12&\n\x08metadata\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\xcb\x01\n\x17PostTestStartUpResponse\x12\x43\n\x06status\x18\x01 \x01(\x0e\x32\x33.chromiumos.test.api.PostTestStartUpResponse.Status\"k\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTATUS_SUCCESS\x10\x01\x12\x1a\n\x16STATUS_INVALID_REQUEST\x10\x02\x12\x19\n\x15STATUS_STARTUP_FAILED\x10\x03\"C\n\x12RunActivityRequest\x12-\n\x07request\x18\x01 \x01(\x0b\x32\x1c.chromiumos.test.api.Request\"\xd1\x03\n\x07Request\x12\x44\n\x13get_fw_info_request\x18\x01 \x01(\x0b\x32%.chromiumos.test.api.GetFWInfoRequestH\x00\x12Q\n\x1aget_files_from_dut_request\x18\x02 \x01(\x0b\x32+.chromiumos.test.api.GetFilesFromDUTRequestH\x00\x12\x46\n\x14get_gfx_info_request\x18\x03 \x01(\x0b\x32&.chromiumos.test.api.GetGfxInfoRequestH\x00\x12\x46\n\x14get_avl_info_request\x18\x04 \x01(\x0b\x32&.chromiumos.test.api.GetAvlInfoRequestH\x00\x12\x46\n\x14get_gsc_info_request\x18\x05 \x01(\x0b\x32&.chromiumos.test.api.GetGscInfoRequestH\x00\x12J\n\x16get_servo_info_request\x18\x06 \x01(\x0b\x32(.chromiumos.test.api.GetServoInfoRequestH\x00\x42\t\n\x07request\"\xaa\x01\n\x14RunActivitiesRequest\x12.\n\x08requests\x18\x01 \x03(\x0b\x32\x1c.chromiumos.test.api.Request\x12\x37\n\ndut_server\x18\x02 \x01(\x0b\x32#.chromiumos.test.lab.api.IpEndpoint\x12)\n\x0btest_result\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"T\n\x15RunActivitiesResponse\x12;\n\tresponses\x18\x01 \x03(\x0b\x32(.chromiumos.test.api.RunActivityResponse\"\x12\n\x10GetFWInfoRequest\"\'\n\x16GetFilesFromDUTRequest\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"\x13\n\x11GetGfxInfoRequest\"\x91\x01\n\x11GetAvlInfoRequest\x12K\n\tavl_files\x18\x01 \x03(\x0b\x32\x34.chromiumos.test.api.GetAvlInfoRequest.AvlFilesEntryB\x02\x18\x01\x1a/\n\rAvlFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x91\x01\n\x11GetGscInfoRequest\x12K\n\tgsc_files\x18\x01 \x03(\x0b\x32\x34.chromiumos.test.api.GetGscInfoRequest.GscFilesEntryB\x02\x18\x01\x1a/\n\rGscFilesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x15\n\x13GetServoInfoRequest\"\xea\x03\n\x13RunActivityResponse\x12\x46\n\x14get_fw_info_response\x18\x01 \x01(\x0b\x32&.chromiumos.test.api.GetFWInfoResponseH\x00\x12S\n\x1bget_files_from_dut_response\x18\x02 \x01(\x0b\x32,.chromiumos.test.api.GetFilesFromDUTResponseH\x00\x12H\n\x15get_gfx_info_response\x18\x03 \x01(\x0b\x32\'.chromiumos.test.api.GetGfxInfoResponseH\x00\x12H\n\x15get_avl_info_response\x18\x04 \x01(\x0b\x32\'.chromiumos.test.api.GetAvlInfoResponseH\x00\x12H\n\x15get_gsc_info_response\x18\x05 \x01(\x0b\x32\'.chromiumos.test.api.GetGscInfoResponseH\x00\x12L\n\x17get_servo_info_response\x18\x06 \x01(\x0b\x32).chromiumos.test.api.GetServoInfoResponseH\x00\x42\n\n\x08response\"m\n\x11GetFWInfoResponse\x12\x0f\n\x07ro_fwid\x18\x01 \x01(\t\x12\x0f\n\x07rw_fwid\x18\x02 \x01(\t\x12\x16\n\x0ekernel_version\x18\x03 \x01(\t\x12\x0e\n\x06gsc_ro\x18\x04 \x01(\t\x12\x0e\n\x06gsc_rw\x18\x05 \x01(\t\"I\n\x17GetFilesFromDUTResponse\x12.\n\x08\x66ile_map\x18\x01 \x03(\x0b\x32\x1c.chromiumos.test.api.FileMap\"3\n\x07\x46ileMap\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x15\n\rfile_location\x18\x02 \x01(\t\"\x92\x01\n\x12GetGfxInfoResponse\x12J\n\ngfx_labels\x18\x01 \x03(\x0b\x32\x36.chromiumos.test.api.GetGfxInfoResponse.GfxLabelsEntry\x1a\x30\n\x0eGfxLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xad\x01\n\x12GetAvlInfoResponse\x12H\n\tavl_infos\x18\x01 \x03(\x0b\x32\x35.chromiumos.test.api.GetAvlInfoResponse.AvlInfosEntry\x1aM\n\rAvlInfosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.chromiumos.test.api.AvlInfo:\x02\x38\x01\"X\n\x07\x41vlInfo\x12\x16\n\x0e\x61vl_part_model\x18\x01 \x01(\t\x12\x19\n\x11\x61vl_part_firmware\x18\x02 \x01(\t\x12\x1a\n\x12\x61vl_component_type\x18\x03 \x01(\t\"\xa5\x01\n\x12GetGscInfoResponse\x12H\n\tgsc_infos\x18\x01 \x03(\x0b\x32\x35.chromiumos.test.api.GetGscInfoResponse.GscInfosEntry\x1a\x45\n\rGscInfosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"@\n\x14GetServoInfoResponse\x12(\n\nservo_info\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any2\xc6\x02\n\x0fPostTestService\x12\x64\n\x07StartUp\x12+.chromiumos.test.api.PostTestStartUpRequest\x1a,.chromiumos.test.api.PostTestStartUpResponse\x12\x65\n\x0bRunActivity\x12\'.chromiumos.test.api.RunActivityRequest\x1a(.chromiumos.test.api.RunActivityResponse\"\x03\x88\x02\x01\x12\x66\n\rRunActivities\x12).chromiumos.test.api.RunActivitiesRequest\x1a*.chromiumos.test.api.RunActivitiesResponseB/Z-go.chromium.org/chromiumos/config/go/test/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chromiumos.test.api.post_test_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-go.chromium.org/chromiumos/config/go/test/api'
  _GETAVLINFOREQUEST_AVLFILESENTRY._options = None
  _GETAVLINFOREQUEST_AVLFILESENTRY._serialized_options = b'8\001'
  _GETAVLINFOREQUEST.fields_by_name['avl_files']._options = None
  _GETAVLINFOREQUEST.fields_by_name['avl_files']._serialized_options = b'\030\001'
  _GETGSCINFOREQUEST_GSCFILESENTRY._options = None
  _GETGSCINFOREQUEST_GSCFILESENTRY._serialized_options = b'8\001'
  _GETGSCINFOREQUEST.fields_by_name['gsc_files']._options = None
  _GETGSCINFOREQUEST.fields_by_name['gsc_files']._serialized_options = b'\030\001'
  _GETGFXINFORESPONSE_GFXLABELSENTRY._options = None
  _GETGFXINFORESPONSE_GFXLABELSENTRY._serialized_options = b'8\001'
  _GETAVLINFORESPONSE_AVLINFOSENTRY._options = None
  _GETAVLINFORESPONSE_AVLINFOSENTRY._serialized_options = b'8\001'
  _GETGSCINFORESPONSE_GSCINFOSENTRY._options = None
  _GETGSCINFORESPONSE_GSCINFOSENTRY._serialized_options = b'8\001'
  _POSTTESTSERVICE.methods_by_name['RunActivity']._options = None
  _POSTTESTSERVICE.methods_by_name['RunActivity']._serialized_options = b'\210\002\001'
  _globals['_POSTTESTSTARTUPREQUEST']._serialized_start=138
  _globals['_POSTTESTSTARTUPREQUEST']._serialized_end=259
  _globals['_POSTTESTSTARTUPRESPONSE']._serialized_start=262
  _globals['_POSTTESTSTARTUPRESPONSE']._serialized_end=465
  _globals['_POSTTESTSTARTUPRESPONSE_STATUS']._serialized_start=358
  _globals['_POSTTESTSTARTUPRESPONSE_STATUS']._serialized_end=465
  _globals['_RUNACTIVITYREQUEST']._serialized_start=467
  _globals['_RUNACTIVITYREQUEST']._serialized_end=534
  _globals['_REQUEST']._serialized_start=537
  _globals['_REQUEST']._serialized_end=1002
  _globals['_RUNACTIVITIESREQUEST']._serialized_start=1005
  _globals['_RUNACTIVITIESREQUEST']._serialized_end=1175
  _globals['_RUNACTIVITIESRESPONSE']._serialized_start=1177
  _globals['_RUNACTIVITIESRESPONSE']._serialized_end=1261
  _globals['_GETFWINFOREQUEST']._serialized_start=1263
  _globals['_GETFWINFOREQUEST']._serialized_end=1281
  _globals['_GETFILESFROMDUTREQUEST']._serialized_start=1283
  _globals['_GETFILESFROMDUTREQUEST']._serialized_end=1322
  _globals['_GETGFXINFOREQUEST']._serialized_start=1324
  _globals['_GETGFXINFOREQUEST']._serialized_end=1343
  _globals['_GETAVLINFOREQUEST']._serialized_start=1346
  _globals['_GETAVLINFOREQUEST']._serialized_end=1491
  _globals['_GETAVLINFOREQUEST_AVLFILESENTRY']._serialized_start=1444
  _globals['_GETAVLINFOREQUEST_AVLFILESENTRY']._serialized_end=1491
  _globals['_GETGSCINFOREQUEST']._serialized_start=1494
  _globals['_GETGSCINFOREQUEST']._serialized_end=1639
  _globals['_GETGSCINFOREQUEST_GSCFILESENTRY']._serialized_start=1592
  _globals['_GETGSCINFOREQUEST_GSCFILESENTRY']._serialized_end=1639
  _globals['_GETSERVOINFOREQUEST']._serialized_start=1641
  _globals['_GETSERVOINFOREQUEST']._serialized_end=1662
  _globals['_RUNACTIVITYRESPONSE']._serialized_start=1665
  _globals['_RUNACTIVITYRESPONSE']._serialized_end=2155
  _globals['_GETFWINFORESPONSE']._serialized_start=2157
  _globals['_GETFWINFORESPONSE']._serialized_end=2266
  _globals['_GETFILESFROMDUTRESPONSE']._serialized_start=2268
  _globals['_GETFILESFROMDUTRESPONSE']._serialized_end=2341
  _globals['_FILEMAP']._serialized_start=2343
  _globals['_FILEMAP']._serialized_end=2394
  _globals['_GETGFXINFORESPONSE']._serialized_start=2397
  _globals['_GETGFXINFORESPONSE']._serialized_end=2543
  _globals['_GETGFXINFORESPONSE_GFXLABELSENTRY']._serialized_start=2495
  _globals['_GETGFXINFORESPONSE_GFXLABELSENTRY']._serialized_end=2543
  _globals['_GETAVLINFORESPONSE']._serialized_start=2546
  _globals['_GETAVLINFORESPONSE']._serialized_end=2719
  _globals['_GETAVLINFORESPONSE_AVLINFOSENTRY']._serialized_start=2642
  _globals['_GETAVLINFORESPONSE_AVLINFOSENTRY']._serialized_end=2719
  _globals['_AVLINFO']._serialized_start=2721
  _globals['_AVLINFO']._serialized_end=2809
  _globals['_GETGSCINFORESPONSE']._serialized_start=2812
  _globals['_GETGSCINFORESPONSE']._serialized_end=2977
  _globals['_GETGSCINFORESPONSE_GSCINFOSENTRY']._serialized_start=2908
  _globals['_GETGSCINFORESPONSE_GSCINFOSENTRY']._serialized_end=2977
  _globals['_GETSERVOINFORESPONSE']._serialized_start=2979
  _globals['_GETSERVOINFORESPONSE']._serialized_end=3043
  _globals['_POSTTESTSERVICE']._serialized_start=3046
  _globals['_POSTTESTSERVICE']._serialized_end=3372
# @@protoc_insertion_point(module_scope)