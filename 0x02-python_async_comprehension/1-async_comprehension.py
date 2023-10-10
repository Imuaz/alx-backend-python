#!/usr/bin/env python3
''' Asynchronous Module task 1'''

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''function that returns 10 random numbers'''
    return [ran_number async for ran_number in async_generator()]
