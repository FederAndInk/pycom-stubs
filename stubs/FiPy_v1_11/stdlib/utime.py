"""
Module: 'utime' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from typing import Optional, Union, overload


@overload
def timezone() -> int:
    ...

@overload
def timezone(h: int):
    ...


def timezone(h: int | None = None) -> int | None:
    ...


def gmtime(secs: Optional[int] = None) -> tuple[int, int, int, int, int, int, int, int]:
    """
    Converts a time expressed in seconds since the Epoch into an 8-tuple which
    contains:

    * ``year``
    * ``month``
    * ``mday``
    * ``hour``
    * ``minute``
    * ``second``
    * ``weekday``
    * ``yearday``

    :param secs: The time to convert. If not provided or ``None``, then the
        current time from the RTC is used.

    :return: The tuple containing the converted time.
    """
    ...


def localtime(secs: Optional[int] = None) -> tuple[int, int, int, int, int, int, int, int]:
    """
    Converts a time expressed in seconds since the Epoch into an 8-tuple which
    contains:

    * ``year``
    * ``month``
    * ``mday``
    * ``hour``
    * ``minute``
    * ``second``
    * ``weekday``
    * ``yearday``

    :param secs: The time to convert. If not provided or ``None``, then the
        current time from the RTC is used.

    :return: The tuple containing the converted time.
    """
    ...


def mktime(local_time: tuple[int, int, int, int, int, int, int, int]) -> int:
    """
    This is inverse function of localtime. Its argument is a full 8-tuple
    which expresses a time as per localtime. It returns an integer which is
    the number of seconds since Jan 1, 2000.

    :param local_time: Full 8-tuple which expresses a time as per localtime.

    :return: Amount of seconds since Epoch for the given time.
    """
    ...


def time() -> int:
    """
    Returns the number of seconds, as an integer, since the Epoch, assuming
    that underlying RTC is set and maintained. If an RTC is not set, this
    function returns number of seconds since a port-specific reference point
    in time (for embedded boards without a battery-backed RTC, usually since
    power up or reset).

    If you want to develop portable MicroPython application, you should not
    rely on this function to provide higher than second precision. If you need
    higher precision, use ``ticks_ms()`` and ``ticks_us()`` functions, if you
    need calendar time, ``localtime()`` without an argument is a better choice.

    :return: Number of seconds, as an integer, since the Epoch.
    """
    ...


def sleep(seconds: Union[int, float]) -> None:
    """
    Sleeps for the given number of seconds. Some boards may accept seconds
    as a floating-point number to sleep for a fractional number of seconds.
    Note that other boards may not accept a floating-point argument, for
    compatibility with them use ``sleep_ms()`` and ``sleep_us()`` functions.

    :param seconds: Amount of time to sleep for.
    """
    ...


def sleep_ms(ms: int) -> None:
    """
    Delays for given number of milliseconds, should be positive or 0.

    :param ms: Delay in milliseconds.
    """
    ...


def sleep_us(us: int) -> None:
    """
    Delays for given number of microseconds, should be positive or 0.

    :param us: Delay in microseconds
    """
    ...


def ticks_ms() -> int:
    """
    Returns the uptime of the XBee module in milliseconds.

    :return: The uptime of the module in milliseconds.
    """
    ...


def ticks_us() -> int:
    """
    Returns the uptime of the XBee module in microseconds.

    :return: The uptime of the module in microseconds.
    """
    ...


def ticks_cpu() -> int:
    """
    Returns the uptime of the module in microseconds but with a higher
    resolution (faster).

    :return: The uptime of the module in microseconds.
    """
    ...


def ticks_add(ticks: int, delta: int) -> int:
    """
    Offsets ticks value by a given number, which can be either positive or
    negative. Given a ticks value, this function allows to calculate ticks
    value delta ticks before or after it, following modular-arithmetic
    definition of tick values (see ``ticks_ms()``).

    This method is useful for calculating deadlines for events/tasks.

    **Note**: You must use ``ticks_diff()`` function to work with deadlines.

    :param ticks: Number obtained from a direct result of call to
        ``ticks_ms()``, ``ticks_us()``, or ``ticks_cpu()`` functions (or from
        previous call to ``ticks_add()``)
    :param delta: Arbitrary integer number or numeric expression.

    :return: Returns the result of the add operation.
    """
    ...


def ticks_diff(ticks1: int, ticks2: int) -> int:
    """
    Measures the period (ticks) difference between values returned from
    ``ticks_ms()``, ``ticks_us()``, or ``ticks_cpu()`` functions, as a signed
    value which may wrap around, so directly subtracting them is not supported.

    The argument order is the same as for subtraction operator,
    ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.

    :param ticks1: Ticks that precede in time the value of ``ticks2``.
    :param ticks2: Second (newer) ticks value.

    :return: The difference between the given ticks values.
    """
    ...
