# -*- coding: utf-8 -*- 
"""
Create on : 2022/11/12
@Author   : Xiao QingLin 
@File    : 9_Python_Iterator_Generator  
"""
from abc import abstractmethod
from collections import UserList
from collections.abc import Reversible
from collections.abc import Collection

"""
UserList(MutableSequence[_T])
MutableSequence(Sequence)
Sequence(Reversible, Collection)
"""


class Sequence(Reversible, Collection):
    """All the operations on a read-only sequence.

    Concrete subclasses must override __new__ or __init__,
    __getitem__, and __len__.
    """

    __slots__ = ()

    # Tell ABCMeta.__new__ that this class should have TPFLAGS_SEQUENCE set.
    __abc_tpflags__ = 1 << 5  # Py_TPFLAGS_SEQUENCE

    @abstractmethod
    def __getitem__(self, index):
        raise IndexError

    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return
