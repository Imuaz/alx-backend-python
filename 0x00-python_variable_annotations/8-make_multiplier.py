#!/usr/bin/env python3
'''
annotated functions module
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' takes a float multiplier and returns /xmultiplies float'''
    def multiplier_function(x: float) -> float:
        ''''the function that multiplies'''
        return x * multiplier
    return multiplier_function
