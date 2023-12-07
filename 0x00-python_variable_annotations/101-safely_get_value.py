#!/usr/bin/env python3
"""
Given the parameters and the return values,
add type annotations to the function
Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Union, TypeVar, Any, Mapping
T = TypeVar('T')
ret = Union[Any, T]
d = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: d = None) -> ret:
    """
    Returns a value given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
