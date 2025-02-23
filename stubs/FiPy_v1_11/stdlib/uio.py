"""
Module: 'uio' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from typing import Any, Callable, Literal, Optional, Union, overload

from _typeshed import AnyPath, OpenBinaryMode, OpenTextMode


class _IOBase(object):
  """
  The abstract base class for all I/O classes, acting on streams of bytes.
  There is no public constructor.
  """

  def read(self, size: int = -1) -> bytes:
    """
    Reads up to ``size`` bytes from the object and returns them. As a
    convenience, if ``size`` is unspecified or ``-1``, all bytes until
    end-of-file (EOF) are returned.

    :param size: Maximum number of bytes to read.

    :return: Read bytes.
    """
    ...

  def readinto(self, b: Any) -> int:
    """
    Reads bytes into a pre-allocated, writable bytes-like object ``b``,
    and returns the number of bytes read.

    :param b: Writable bytes-like object where read bytes will be placed.

    :return: Number of bytes read.
    """
    ...

  def readline(self, size: int = -1) -> bytes:
    """
    Reads and returns one line from the stream. If ``size`` is specified,
    at most ``size`` bytes are read.

    :param size: Maximum number of bytes to read.

    :return: Read line in bytes.
    """
    ...

  def write(self, b: Any) -> int:
    """
    Writes the given bytes-like object, ``b``, to the underlying raw
    stream, and returns the number of bytes written.

    :param b: Bytes-like object to write in the stream.

    :return: The number of bytes written.
    """
    ...

  def seek(self, offset: int, whence: int = 0) -> int:
    """
    Changes the stream position to the given byte ``offset``. ``offset``
    is interpreted relative to the position indicated by ``whence``. The
    default value for ``whence`` is ``0``. Values for whence are:

    * ``0`` – start of the stream (the default); offset should be zero or
      positive.
    * ``1`` – current stream position; offset may be negative.
    * ``2`` – end of the stream; offset is usually negative.

    **Note**: Seeking is disabled when writing to secure files.

    :param offset: New stream position relative to the position indicated
        by ``whence``.
    :param whence: Initial position of the stream.

    :return: The new absolute position of the stream.
    """
    ...

  def tell(self) -> int:
    """
    Returns the current stream position.

    :return: The current stream position.
    """
    ...

  def flush(self) -> None:
    """
    Flushes the write buffers of the stream if applicable. This does
    nothing for read-only streams.
    """
    ...

  def close(self) -> None:
    """
    Flushes and closes the stream. This does nothing if the file is
    already closed.
    """
    ...

  def __enter__(self) -> Any:
    """
    """
    ...

  def __exit__(self) -> None:
    """
    """
    ...


class BytesIO(_IOBase):
  """
  A stream implementation using an in-memory bytes buffer. The buffer is
  discarded when the ``close()`` method is called.
  """

  def __init__(self, initial_bytes: Any = None) -> None:
    """
    Class constructor. Instantiates a ``BytesIO`` object with an optional
    initial data.

    :param initial_bytes: bytes-like-object with initial data.
    """
    ...

  def getvalue(self) -> bytes:
    """
    Gets the current contents of the underlying buffer which holds data.

    :return: Current contents of the underlying buffer in bytes format.
    """
    ...


class FileIO(_IOBase):
  """
  Represents an OS-level file containing bytes data.
  """

  def __init__(self, file: str, *, mode: str = "r", buffering: int = -1,
               encoding: str | None = None) -> None:
    """
    Class constructor. Instantiates a ``FileIO`` object with the provided
    parameters.

    :param file: The file name.
    :param mode: Optional string that specifies the mode in which the file
        is opened. It defaults to **'r'** which means open for reading in
        text mode. Other common values are **'w'** for writing (truncating
        the file if it already exists), **'x'** for exclusive creation,
        **'a'** for appending all writes append to the end of the file
        regardless of the current seek position and **'*'** for opening a
        secure file for writing (only available on modules that support
        secure files).
    :param buffering: Optional integer used to set the buffering policy.
        Pass **0** to switch buffering off (only allowed in binary mode),
        **1** to select line buffering (only usable in text mode), and an
        **integer > 1** to indicate the size in bytes of a fixed-size chunk
        buffer.
    :param encoding: Gives the name of the encoding that the stream will be
        decoded or encoded with.
    """
    ...

  def readlines(self) -> list[str]:
    """
    Reads and returns a list of lines from the stream.

    **Note**: It is already possible to iterate on file objects using
        ``for line in file: ...`` without calling ``file.readlines()``.

    :return: A list of lines from the stream.
    """
    ...

  def __del__(self) -> None:
    """
    Prepares for object destruction. Calls the instance's ``close()``
    method.
    """
    ...


class StringIO(_IOBase):
  """
  An in-memory stream for text I/O. The text buffer is discarded when the
  ``close()`` method is called.
  """

  def __init__(self, *, initial_value: str = "", newline: str = "\n") -> None:
    """
    Class constructor. Instantiates a ``StringIO`` object with the provided
    parameters.

    The initial value of the buffer can be set by providing
    ``initial_value``. If newline translation is enabled, newlines
    will be encoded as if by ``write()``. The stream is positioned at the
    start of the buffer.

    :param initial_value: String with the initial value of the buffer.
    :param newline: Controls how line endings are handled. It can be
        ``None``, ``''``, ``'\n'``, ``'\r'``, and ``'\r\n'``.
    """
    ...

  def getvalue(self) -> str:
    """
    Returns a string containing the entire contents of the buffer.
    Newlines are decoded as if by ``read()``, although the stream position
    is not changed.

    :return: String with the contents of the buffer.
    """
    ...


class TextIOWrapper(_IOBase):
  """
  Buffered text stream that provides a character and line based interface to
  stream I/O.
  """

  def __init__(self, file: str, *, mode: str = "r", buffering: int = -1,
               encoding: str | None = None) -> None:
    """
    Class constructor. Instantiates a ``TextIOWrapper`` with the provided
    parameters.

    :param file: Name of the file to stream.
    :param mode: Optional string that specifies the mode in which the file
        is opened. It defaults to **'r'** which means open for reading in
        text mode. Other common values are **'w'** for writing (truncating
        the file if it already exists), **'x'** for exclusive creation,
        **'a'** for appending all writes append to the end of the file
        regardless of the current seek position and **'*'** for opening a
        secure file for writing (only available on modules that support
        secure files).
    :param buffering: Optional integer used to set the buffering policy.
        Pass **0** to switch buffering off (only allowed in binary mode),
        **1** to select line buffering (only usable in text mode), and an
        **integer > 1** to indicate the size in bytes of a fixed-size chunk
        buffer.
    :param encoding: Gives the name of the encoding that the stream will be
        decoded or encoded with.
    """
    ...

  def readlines(self) -> list[str]:
    """
    Reads and returns a list of lines from the stream.

    **Note**: It is already possible to iterate on file objects using
        ``for line in file: ...`` without calling ``file.readlines()``.

    :return: A list of lines from the stream.
    """
    ...

  def __del__(self) -> None:
    """
    Prepares for object destruction. Calls the instance's ``close()``
    method.
    """
    ...


_OpenFile = Union[AnyPath, int]
_Opener = Callable[[str, int], int]

@overload
def open(
    file: _OpenFile,
    mode: OpenTextMode = ...,
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
) -> TextIOWrapper: 
    """
    Opens a file. Builtin ``open()`` function is an alias to
    ``uio.open(file, mode='r')`` which returns a file object a ``uio.FileIO``
    object for binary modes and a ``uio.TextIOWrapper`` object for text modes.
    If the file cannot be opened, an ``OSError`` is raised.

    :param file: Path-like object giving the path absolute or relative to the
        current working directory of the file to be opened.
    :param mode: Optional string that specifies the mode in which the file is
        opened. It defaults to **'r'** which means open for reading in text
        mode. Other common values are **'w'** for writing (truncating the file
        if it already exists), **'x'** for exclusive creation, **'a'** for
        appending all writes append to the end of the file regardless of the
        current seek position and **'*'** for opening a secure file for writing
        (only available on modules that support secure files).
    :param buffering: Optional integer used to set the buffering policy. Pass
        **0** to switch buffering off (only allowed in binary mode), **1** to
        select line buffering (only usable in text mode), and an
        **integer > 1** to indicate the size in bytes of a fixed-size chunk
        buffer.
    :param encoding: The name of the encoding used to decode or encode the
        file. This should only be used in text mode.

    :return: A file object.
    """
    ...

# Unbuffered binary mode: returns a FileIO


@overload
def open(
    file: _OpenFile,
    mode: OpenBinaryMode,
    buffering: Literal[0],
    encoding: None = ...,
    errors: None = ...,
    newline: None = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
) -> FileIO:
    """
    Opens a file. Builtin ``open()`` function is an alias to
    ``uio.open(file, mode='r')`` which returns a file object a ``uio.FileIO``
    object for binary modes and a ``uio.TextIOWrapper`` object for text modes.
    If the file cannot be opened, an ``OSError`` is raised.

    :param file: Path-like object giving the path absolute or relative to the
        current working directory of the file to be opened.
    :param mode: Optional string that specifies the mode in which the file is
        opened. It defaults to **'r'** which means open for reading in text
        mode. Other common values are **'w'** for writing (truncating the file
        if it already exists), **'x'** for exclusive creation, **'a'** for
        appending all writes append to the end of the file regardless of the
        current seek position and **'*'** for opening a secure file for writing
        (only available on modules that support secure files).
    :param buffering: Optional integer used to set the buffering policy. Pass
        **0** to switch buffering off (only allowed in binary mode), **1** to
        select line buffering (only usable in text mode), and an
        **integer > 1** to indicate the size in bytes of a fixed-size chunk
        buffer.
    :param encoding: The name of the encoding used to decode or encode the
        file. This should only be used in text mode.

    :return: A file object.
    """
    ...


def open(
    file: _OpenFile,
    mode: OpenBinaryMode | OpenTextMode = ...,
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    closefd: bool = ...,
    opener: Optional[_Opener] = ...,
) -> FileIO | TextIOWrapper: ...
