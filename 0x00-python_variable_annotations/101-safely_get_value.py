#!/usr/bin/env python3
'''
annotated module
'''
import typing

T = typing.TypeVar('T')


def safely_get_value(
        dct: typing.Mapping, key: typing.Any, default: xtyping.Union[T, None] =
        None) -> typing.Union[typing.Any, T]:
    ''''annotated function'''
    if key in dct:
        return dct[key]
    else:
        return default
