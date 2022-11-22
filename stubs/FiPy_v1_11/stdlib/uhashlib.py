"""

hashing algorithms. See: https://docs.micropython.org/en/v1.19.1/library/hashlib.html

|see_cpython_module| :mod:`python:hashlib` https://docs.python.org/3/library/hashlib.html .

This module implements binary data hashing algorithms. The exact inventory
of available algorithms depends on a board. Among the algorithms which may
be implemented:

* SHA256 - The current generation, modern hashing algorithm (of SHA2 series).
    It is suitable for cryptographically-secure purposes. Included in the
    MicroPython core and any board is recommended to provide this, unless
    it has particular code size constraints.

* SHA1 - A previous generation algorithm. Not recommended for new usages,
    but SHA1 is a part of number of Internet standards and existing
    applications, so boards targeting network connectivity and
    interoperability will try to provide this.

* MD5 - A legacy algorithm, not considered cryptographically secure. Only
    selected boards, targeting interoperability with legacy applications,
    will offer this.
"""

# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2
from typing import Any, Optional


class md5:
    """
    Create an md5 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...


class sha1:
    """
    Create an sha1 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...


class sha224:
    """
    Create an sha224 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...


class sha256:
    """
    Create an sha256 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...


class sha384:
    """
    Create an sha384 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...


class sha512:
    """
    Create an sha512 hasher object and optionally feed ``data`` into it.
    """

    def digest(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def __init__(self, data: Optional[Any] = None) -> None: ...
