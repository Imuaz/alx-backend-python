#!/usr/bin/env python3
'''
annotated function module
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' function that return multiple'''
    squared_value = float(v) ** 2
    return k, squared_value
