#!/usr/bin/env python3
'''
annotatade module
'''
from typing import Sequence, Any


def zoom_array(lst: Sequence[Any], factor: int = 2) -> Sequence[Any]:
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
