# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Entities

from .flatbuffers import *
from .flatbuffers.compat import import_numpy
np = import_numpy()

class Vec4(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 16

    # Vec4
    def Init(self, buf, pos):
        self._tab = table.Table(buf, pos)

    # Vec4
    def X(self): return self._tab.Get(number_types.Float32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(0))
    # Vec4
    def Y(self): return self._tab.Get(number_types.Float32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(4))
    # Vec4
    def Z(self): return self._tab.Get(number_types.Float32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(8))
    # Vec4
    def R(self): return self._tab.Get(number_types.Float32Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(12))

def CreateVec4(builder, x, y, z, r):
    builder.Prep(4, 16)
    builder.PrependFloat32(r)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    return builder.Offset()