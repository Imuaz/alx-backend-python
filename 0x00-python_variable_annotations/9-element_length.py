#!/usr/bin/env python3
'''
annotated module
'''
from typing import Tuple, Iterable, Sequence, List,


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''annotated function'''
    return [(i, len(i)) for i in lst]
