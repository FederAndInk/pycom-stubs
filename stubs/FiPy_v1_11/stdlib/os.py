"""
Module: 'os' on FiPy v1.11

The `uos` module contains functions for filesystem access and `urandom` function.

Port Specifics:

The filesystem has `/` as the root directory and the available physical drives are accessible from here. They are currently:

    - `/flash` – the internal flash filesystem
    - `/sd` – the SD card (if it exists)
"""
from uos import *
