"""
Module: 'uos' on FiPy v1.11

The `uos` module contains functions for filesystem access and `urandom` function.

Port Specifics:

The filesystem has `/` as the root directory and the available physical drives are accessible from here. They are currently:

    - `/flash` – the internal flash filesystem
    - `/sd` – the SD card (if it exists)
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2
from typing import (Any, Callable, Iterator, List, Literal, NamedTuple,
                    Optional, Tuple, Union, overload)

from machine import SD
from uio import FileIO, TextIOWrapper

from ._typeshed import AnyPath, OpenBinaryMode, OpenTextMode

_OpenFile = Union[AnyPath, int]
_Opener = Callable[[str, int], int]


class mkfat:
  '''
  '''

  def __init__(self, blockdev: SD) -> None:
    ...

  def ilistdir(self, path: str = ".") -> Iterator[Tuple[str, int, int, int]]:
    """
    Returns an iterator which then yields tuples corresponding to the entries
    in the directory that it is listing. With no argument it lists the current
    directory, otherwise it lists the directory given by ``path``.

    The tuples have the form ``(name, type, inode[, size])``:

    * ``name`` is a string (or bytes if dir is a bytes object) and is the name
        of the entry.
    * ``type`` is an integer that specifies the type of the entry, with 0x4000
        for directories and 0x8000 for regular files.
    * ``inode`` is an integer corresponding to the inode of the file, and may
        be 0 for filesystems that don't have such a notion.
    * Some platforms may return a 4-tuple that includes the entry's size. For
        file entries, ``size`` is an integer representing the size of the file or
        -1 if unknown. Its meaning is currently undefined for directory entries.

    :param path: Path to list its elements.

    :return: An iterator with a tuple for each entry in the path.
    """
    ...

  def statvfs(self, path: str) -> Tuple[int, int, int, int, int, int, int, int, int, int]:
    """
    Gets the status of a fileystem.

    Returns a tuple with the filesystem information in the following order:

    * ``f_bsize`` – file system block size
    * ``f_frsize`` – fragment size
    * ``f_blocks`` – size of fs in f_frsize units
    * ``f_bfree`` – number of free blocks
    * ``f_bavail`` – number of free blocks for unpriviliged users
    * ``f_files`` – number of inodes
    * ``f_ffree`` – number of free inodes
    * ``f_favail`` – number of free inodes for unpriviliged users
    * ``f_flag`` – mount flags
    * ``f_namemax`` – maximum filename length

    :param path: Path of the filesystem to get its status.

    :return: Tuple with the status of a filesystem.
    """
    ...

  def chdir(self, path: str) -> None:
    """
    Changes current directory.

    :param path: Path to change to.
    """
    ...

  def fsformat(self):
    pass

  def getcwd(self) -> str:
    """
    Gets the current directory.

    :return: Current directory.
    """
    ...

  def getfree(self, path: str) -> int:
    '''
    Returns the free space (in KiB) in the drive specified by path.
    '''
    ...

  def mkdir(self, path: str) -> None:
    """
    Creates a new directory.

    :param path: Name of the directory to create.
    """
    ...

  def mkfs(self, block_deviceorpath: str):
    '''
    Formats the specified path, must be either `/flash` or `/sd` . A block device can also be passed like an SD object before being mounted.
    '''
    ...

  def mount(self, block_device, mount_point: str, *, readonly=False):
    """
    Mounts a block device (like an SD object) in the specified mount point. Example:

    ```python
    uos.mount(sd, '/sd')
    ```

    Mount the filesystem object *fsobj* at the location in the VFS given by the
    *mount_point* string.  *fsobj* can be a a VFS object that has a ``mount()``
    method, or a block device.  If it's a block device then the filesystem type
    is automatically detected (an exception is raised if no filesystem was
    recognised).  *mount_point* may be ``'/'`` to mount *fsobj* at the root,
    or ``'/<name>'`` to mount it at a subdirectory under the root.

    If *readonly* is ``True`` then the filesystem is mounted read-only.

    During the mount process the method ``mount()`` is called on the filesystem
    object.

    Will raise ``OSError(EPERM)`` if *mount_point* is already mounted.
    """
    ...

  @overload
  def open(self,
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
  def open(self,
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

  def open(self,
           file: _OpenFile,
           mode: OpenBinaryMode | OpenTextMode = ...,
           buffering: int = ...,
           encoding: Optional[str] = ...,
           errors: Optional[str] = ...,
           newline: Optional[str] = ...,
           closefd: bool = ...,
           opener: Optional[_Opener] = ...,
           ) -> FileIO | TextIOWrapper: ...

  def remove(self, path: str) -> None:
    """
    Removes a file.

    :param path: Path of the file to remove.
    """
    ...

  def rename(self, old_path: str, new_path: str) -> None:
    """
    Renames a file or directory.

    :param old_path: Name of the file to rename.
    :param new_path: New name of the file.
    """
    ...

  def rmdir(self, dir: str) -> None:
    """
    Removes a directory. Fails if ``dir`` is not empty.

    :param dir: Path of the directory to remove.
    """
    ...

  def stat(self, path: str) -> Tuple[int, int, int, int, int, int, int, int, int, int]:
    '''
    Get the status of a file or directory.

    The return value is a tuple with the following 10 values, in order:

    - `st_mode` : protection bits.
    - `st_ino` : `inode` number. (not implemented, returns 0)
    - `st_dev` : device. (not implemented, returns 0)
    - `st_nlink` : number of hard links. (not implemented, returns 0)
    - `st_uid` : user id of owner. (not implemented, returns 0)
    - `st_gid` : group id of owner. (not implemented, returns 0)
    - `st_size` : size of file in bytes.
    - `st_atime` : time of most recent access.
    - `st_mtime` : time of most recent content modification.
    - `st_ctime` : time of most recent metadata change.
    '''
    ...

  def umount(self, mount_point: str | SD):
    '''
    Unmounts a previously mounted block device from the specified mount point. Example:

    ```python
    uos.umount('/sd')
    ```
    '''
    ...


def fsformat():
  pass


def ilistdir(path: str = ".") -> Iterator[Tuple[str, int, int, int]]:
  """
  Returns an iterator which then yields tuples corresponding to the entries
  in the directory that it is listing. With no argument it lists the current
  directory, otherwise it lists the directory given by ``path``.

  The tuples have the form ``(name, type, inode[, size])``:

  * ``name`` is a string (or bytes if dir is a bytes object) and is the name
      of the entry.
  * ``type`` is an integer that specifies the type of the entry, with 0x4000
      for directories and 0x8000 for regular files.
  * ``inode`` is an integer corresponding to the inode of the file, and may
      be 0 for filesystems that don't have such a notion.
  * Some platforms may return a 4-tuple that includes the entry's size. For
      file entries, ``size`` is an integer representing the size of the file or
      -1 if unknown. Its meaning is currently undefined for directory entries.

  :param path: Path to list its elements.

  :return: An iterator with a tuple for each entry in the path.
  """
  ...


def statvfs(path: str) -> Tuple[int, int, int, int, int, int, int, int, int, int]:
  """
  Gets the status of a fileystem.

  Returns a tuple with the filesystem information in the following order:

  * ``f_bsize`` – file system block size
  * ``f_frsize`` – fragment size
  * ``f_blocks`` – size of fs in f_frsize units
  * ``f_bfree`` – number of free blocks
  * ``f_bavail`` – number of free blocks for unpriviliged users
  * ``f_files`` – number of inodes
  * ``f_ffree`` – number of free inodes
  * ``f_favail`` – number of free inodes for unpriviliged users
  * ``f_flag`` – mount flags
  * ``f_namemax`` – maximum filename length

  :param path: Path of the filesystem to get its status.

  :return: Tuple with the status of a filesystem.
  """
  ...


class _Uname(NamedTuple):
  sysname: str
  nodename: str
  release: str
  version: str
  machine: str
  lorawan: str
  sigfox: str
  pybytes: str


def uname() -> _Uname:
  '''
  Return information about the system, firmware release version, and MicroPython interpreter version.

  Return a tuple (possibly a named tuple) containing information about
  the underlying machine and/or its operating system. The tuple has
  five fields in the following order, each of them being a string:

  * ``sysname`` – the name of the underlying system
  * ``nodename`` – the network name (can be the same as ``sysname``)
  * ``release`` – the version of the underlying system
  * ``version`` – the MicroPython version and build date
  * ``machine`` – an identifier for the underlying hardware (eg board, CPU)

  :return: Tuple with information about the machine or operating system.
  '''
  ...


def chdir(path: str) -> None:
  """
  Changes current directory.

  :param path: Path to change to.
  """
  ...


def getcwd() -> str:
  """
  Gets the current directory.

  :return: Current directory.
  """
  ...


def listdir(path: str = ".") -> List:
  """
  Lists the specified path or the current one if ``path`` is not provided.

  :param path: The path to list. If this parameter is not provided, the
      method lists the current path.

  :return: List containing the name of the elements in the path.
  """
  ...


def mkdir(path: str) -> None:
  """
  Creates a new directory.

  :param path: Name of the directory to create.
  """
  ...


def remove(path: str) -> None:
  """
  Removes a file.

  :param path: Path of the file to remove.
  """
  ...


def rmdir(dir: str) -> None:
  """
  Removes a directory. Fails if ``dir`` is not empty.

  :param dir: Path of the directory to remove.
  """
  ...


def rename(old_path: str, new_path: str) -> None:
  """
  Renames a file or directory.

  :param old_path: Name of the file to rename.
  :param new_path: New name of the file.
  """
  ...


def stat(path: str) -> Tuple[int, int, int, int, int, int, int, int, int, int]:
  '''
  Get the status of a file or directory.

  The return value is a tuple with the following 10 values, in order:

  - `st_mode` : protection bits.
  - `st_ino` : `inode` number. (not implemented, returns 0)
  - `st_dev` : device. (not implemented, returns 0)
  - `st_nlink` : number of hard links. (not implemented, returns 0)
  - `st_uid` : user id of owner. (not implemented, returns 0)
  - `st_gid` : group id of owner. (not implemented, returns 0)
  - `st_size` : size of file in bytes.
  - `st_atime` : time of most recent access.
  - `st_mtime` : time of most recent content modification.
  - `st_ctime` : time of most recent metadata change.
  '''
  ...


def getfree(path: str) -> int:
  '''
  Returns the free space (in KiB) in the drive specified by path.
  '''
  ...


def sync():
  '''
  Sync all filesystems.
  '''
  ...


def urandom(n: int) -> bytes:
  '''
  Return a bytes object with n random bytes.
  '''
  ...


def unlink(path: str) -> None:
  '''
  Alias for the `remove()` method.
  '''
  ...


def mount(block_device: SD, mount_point: str, *, readonly=False):
  """
  Mounts a block device (like an SD object) in the specified mount point. Example:

  ```python
  uos.mount(sd, '/sd')
  ```

  Mount the filesystem object *fsobj* at the location in the VFS given by the
  *mount_point* string.  *fsobj* can be a a VFS object that has a ``mount()``
  method, or a block device.  If it's a block device then the filesystem type
  is automatically detected (an exception is raised if no filesystem was
  recognised).  *mount_point* may be ``'/'`` to mount *fsobj* at the root,
  or ``'/<name>'`` to mount it at a subdirectory under the root.

  If *readonly* is ``True`` then the filesystem is mounted read-only.

  During the mount process the method ``mount()`` is called on the filesystem
  object.

  Will raise ``OSError(EPERM)`` if *mount_point* is already mounted.
  """
  ...


def umount(mount_point: str | SD):
  '''
  Unmounts a previously mounted block device from the specified mount point. Example:

  ```python
  uos.umount('/sd')
  ```
  '''
  ...


def dupterm(stream_object):
  '''
  Duplicate the terminal (the REPL) on the passed stream-like object. The given object must at least implement the `read()` and `write()` methods.
  '''
  ...
