#!/usr/bin/env python3
'''
task 1 module
'''
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> float:
    '''function that reurns list of all delays'''
    delay = []

    tasks = [wait_random(max_delay) for in range(n)]
    result = await asyncio.gather(*tasks)

    for _ in range(n):
        min_delay = min(result)
        delay.append(min_delay)
        result.remove(min_delay)

    return delay
