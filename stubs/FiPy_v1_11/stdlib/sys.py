"""
Module: 'sys' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from types import ModuleType, TracebackType
from typing import Any, Literal, NamedTuple, Union

from uio import FileIO

argv: list
byteorder: Literal["little", "big"]

_ExcInfo = tuple[type[BaseException], BaseException, TracebackType]
_OptExcInfo = Union[_ExcInfo, tuple[None, None, None]]


def exc_info() -> _OptExcInfo:
    ...


def exit(retval=0):
    pass


class _Implementation(NamedTuple):
    name: str
    version: tuple[int, int, int]


implementation: _Implementation
maxsize = 2147483647
modules: dict[str, ModuleType]
path: list[str]
platform = 'FiPy'


stderr: FileIO = Any
stdin: FileIO = Any
stdout: FileIO = Any
version = '3.4.0'
version_info = (3, 4, 0)


def print_exception(exc: BaseException, file=stdout):
    ...
