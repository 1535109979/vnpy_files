# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strategy_server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from a_songbo.vn.proto import account_position_pb2 as account__position__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15strategy_server.proto\x12\x0fstrategy_server\x1a\x16\x61\x63\x63ount_position.proto\"\x9e\x01\n\tRtnRecord\x12\x30\n\x03rtn\x18\x01 \x03(\x0b\x32#.strategy_server.RtnRecord.RtnEntry\x12\x33\n\x0c\x61\x63\x63ount_book\x18\x02 \x01(\x0b\x32\x1d.account_position.AccountBook\x1a*\n\x08RtnEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x19\n\tFlagReply\x12\x0c\n\x04\x66lag\x18\x01 \x01(\x08\x32\xea\x01\n\x08Strategy\x12N\n\x11on_account_update\x12\x1d.account_position.AccountBook\x1a\x1a.strategy_server.FlagReply\x12\x46\n\x0con_order_rtn\x12\x1a.strategy_server.RtnRecord\x1a\x1a.strategy_server.FlagReply\x12\x46\n\x0con_trade_rtn\x12\x1a.strategy_server.RtnRecord\x1a\x1a.strategy_server.FlagReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'strategy_server_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RTNRECORD_RTNENTRY._options = None
  _RTNRECORD_RTNENTRY._serialized_options = b'8\001'
  _RTNRECORD._serialized_start=67
  _RTNRECORD._serialized_end=225
  _RTNRECORD_RTNENTRY._serialized_start=183
  _RTNRECORD_RTNENTRY._serialized_end=225
  _FLAGREPLY._serialized_start=227
  _FLAGREPLY._serialized_end=252
  _STRATEGY._serialized_start=255
  _STRATEGY._serialized_end=489
# @@protoc_insertion_point(module_scope)