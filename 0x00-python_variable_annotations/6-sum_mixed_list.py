#!/usr/bin/env python3
'''
annotated function module
'''
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function that returns sum of int and float as floate'''
    return sum(mxd_lst)
