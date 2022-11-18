import sys
from collections.abc import Callable
from threading import Thread
from types import TracebackType
from typing import Any, NoReturn

from _typeshed import structseq
from typing_extensions import Final, final

error = RuntimeError


def _count() -> int: ...


@final
class LockType:
  def acquire(self, blocking: bool = ..., timeout: float = ...) -> bool: ...
  def release(self) -> None: ...
  def locked(self) -> bool: ...
  def __enter__(self) -> bool: ...

  def __exit__(
      self, type: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
  ) -> None: ...


def start_new_thread(
    function: Callable[..., object], args: tuple[Any, ...], kwargs: dict[str, Any] = ...) -> int: ...


def interrupt_main() -> None: ...
def exit() -> NoReturn: ...
def allocate_lock() -> LockType: ...
def get_ident() -> int: ...
def stack_size(size: int = ...) -> int: ...


TIMEOUT_MAX: float

if sys.version_info >= (3, 8):
  def get_native_id() -> int: ...  # only available on some platforms

  @final
  class _ExceptHookArgs(structseq[Any], tuple[type[BaseException], BaseException | None, TracebackType | None, Thread | None]):
    if sys.version_info >= (3, 10):
      __match_args__: Final = (
          "exc_type", "exc_value", "exc_traceback", "thread")

    @property
    def exc_type(self) -> type[BaseException]: ...
    @property
    def exc_value(self) -> BaseException | None: ...
    @property
    def exc_traceback(self) -> TracebackType | None: ...
    @property
    def thread(self) -> Thread | None: ...
  _excepthook: Callable[[_ExceptHookArgs], Any]
