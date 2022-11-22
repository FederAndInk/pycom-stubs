"""
efficient arrays of numeric data. See: https://docs.micropython.org/en/v1.19.1/library/array.html

|see_cpython_module| :mod:`python:array` https://docs.python.org/3/library/array.html .

Supported format codes: ``b``, ``B``, ``h``, ``H``, ``i``, ``I``, ``l``,
``L``, ``q``, ``Q``, ``f``, ``d`` (the latter 2 depending on the
floating-point support).
"""
from typing import Optional, Any

class array:
    """
    Create array with elements of given type. Initial contents of the
    array are given by *iterable*. If it is not provided, an empty
    array is created.
    """

    def extend(self, iterable) -> Any:
        """
        Append new elements as contained in *iterable* to the end of
        array, growing it.
        """
        ...

    def decode(self, *args, **kwargs) -> Any: ...

    def append(self, val) -> Any:
        """
        Append new element *val* to the end of array, growing it.
        """
        ...

    def __init__(self, typecode, iterable: Optional[Any] = None) -> None:
        """
        Create array with elements of given type. Initial contents of the array are given by an iterable. If it is not provided, an empty array is created. Supported format codes:
    
        - `b` : signed char, 1 byte 
        - `B` : unsigned char, 1 byte 
        - `h` : signed short, 2 bytes 
        - `H` : unsigned short, 2 bytes 
        - `i` : signed int, 2 bytes 
        - `I` : unsigned int, 2 bytes 
        - `l` : signed long, 4 bytes 
        - `L` : unsigned long, 4 bytes 
        - `q` : signed long long, 8 bytes 
        - `Q` : unsigned long long, 8 bytes 
        - `f` : foat, 4 bytes 
        - `d` : double, 8 bytes 
        
        Adapting the typecode to the array-type you want to create can save a lot of space on the microcontroller
        """
        ...
