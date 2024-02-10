# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Entities

from .flatbuffers import *
from .flatbuffers.compat import import_numpy
np = import_numpy()

class LODInfo_A2(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 12

    # LODInfo_A2
    def Init(self, buf, pos):
        self._tab = table.Table(buf, pos)

    # LODInfo_A2
    def Offset(self): return self._tab.Get(number_types.Int32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(0))
    # LODInfo_A2
    def Count(self): return self._tab.Get(number_types.Int32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(4))
    # LODInfo_A2
    def Unk(self): return self._tab.Get(number_types.Int32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(8))

def CreateLODInfo_A2(builder, offset, count, unk):
    builder.Prep(4, 12)
    builder.PrependInt32(unk)
    builder.PrependInt32(count)
    builder.PrependInt32(offset)
    return builder.Offset()