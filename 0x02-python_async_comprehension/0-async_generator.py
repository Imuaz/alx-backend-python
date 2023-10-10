#!/usr/bin/env python3
'''
Module for async_generator coroutine
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''loops 10 times and returns random number b/w 10 and 0'''
    for _ in range(10):
        await asyncio.sleep(1)

        random_number = random.uniform(0, 10)
        yield random_number
