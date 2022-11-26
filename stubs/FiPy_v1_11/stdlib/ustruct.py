"""
Module: 'ustruct' on FiPy v1.11

See [Python struct](https://docs.python.org/3/library/struct.html) for more information.

Supported size/byte order prefixes: `@, <, >, !`.

Supported format codes: `b, B, h, H, i, I, l, L, q, Q, s, P, f, d` (the latter 2 depending on the floating-point support).
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from typing import Any, Tuple


def calcsize(fmt: str) -> int:
  """
  Returns the number of bytes needed to store the given ``fmt``.

  :param fmt: Identifier of the typecode to get its size.

  :return: The number of bytes needed.
  """
  ...


def pack(fmt: str, v1: Any, *vn: Any) -> bytes:
  """
  Returns a bytes object containing the values v1, v2, ... packed according
  to the format string ``fmt``.

  :param fmt: Format string sequence of the values to pack.
  :param v1: Value to pack.
  :param vn: Additional values to pack.

  :return: Bytes object with the values packed according to the given format.
  """
  ...


def pack_into(fmt: str, buff: Any, offset: int, v1: Any, *vn: Any) -> None:
  """
  Packs the values v1, v2, ... according to the format string ``fmt`` and
  writes the packed bytes into the writable buffer ``buf`` starting at
  ``offset`` which can be negative meaning starting from the end.

  **Note**: The offset is a required argument.

  :param fmt: Format string sequence of the values to pack.
  :param buff: Buffer to write the packed values into.
  :param offset: Starting offset to pack values within the buffer.
  :param v1: Value to pack.
  :param vn: Additional values to pack.
  """
  ...


def unpack(fmt: str, buffer: Any) -> Tuple:
  """
  Returns a tuple containing values unpacked according to the format string
  ``fmt``. The buffer's size in bytes must be ``calcsize(fmt)``.

  :param fmt: Format string sequence of the packed values.
  :param buffer: Buffer containing the packed values to unpack.

  :return: Tuple containing the unpacked values.
  """
  ...


def unpack_from(fmt: str, buffer: Any, offset: int = 0) -> None:
  """
  Returns a tuple containing values unpacked according to the format string
  ``fmt``.  The buffer's size, minus ``offset``, must be at least
  ``calcsize(fmt)``.

  :param fmt: Format string sequence of the packed values.
  :param buffer: Buffer containing the packed values to unpack. may be negative to count from the end of buffer
  :param offset: Offset within buffer to start unpacking values.

  :return: Tuple containing the unpacked values.
  """
  ...
