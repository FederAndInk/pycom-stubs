"""
Module: 'time' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

import sys
from typing import Any, Protocol

from _typeshed import structseq
from typing_extensions import Final, Literal, TypeAlias, final

_TimeTuple = tuple[int, int, int, int, int, int, int, int, int]

# Constructor takes an iterable of any type, of length between 9 and 11 elements.
# However, it always *behaves* like a tuple of 9 elements,
# even if an iterable with length >9 is passed.
# https://github.com/python/typeshed/pull/6560#discussion_r767162532


@final
class struct_time(structseq[Any | int], _TimeTuple):
  if sys.version_info >= (3, 10):
    __match_args__: Final = ("tm_year", "tm_mon", "tm_mday", "tm_hour",
                             "tm_min", "tm_sec", "tm_wday", "tm_yday", "tm_isdst")

  @property
  def tm_year(self) -> int: ...
  @property
  def tm_mon(self) -> int: ...
  @property
  def tm_mday(self) -> int: ...
  @property
  def tm_hour(self) -> int: ...
  @property
  def tm_min(self) -> int: ...
  @property
  def tm_sec(self) -> int: ...
  @property
  def tm_wday(self) -> int: ...
  @property
  def tm_yday(self) -> int: ...
  @property
  def tm_isdst(self) -> int: ...
  # These final two properties only exist if a 10- or 11-item sequence was passed to the constructor.
  @property
  def tm_zone(self) -> str: ...
  @property
  def tm_gmtoff(self) -> int: ...


def gmtime(secs: float | None = ...) -> struct_time: ...
def localtime(secs: float | None = ...) -> struct_time: ...
def mktime(t: _TimeTuple | struct_time) -> float: ...
def sleep(secs: float) -> None: ...
def time() -> float: ...


def sleep_ms():
  pass


def sleep_us():
  pass


def ticks_add():
  pass


def ticks_cpu():
  pass


def ticks_diff():
  pass


def ticks_ms():
  pass


def ticks_us():
  pass


def timezone():
  pass
