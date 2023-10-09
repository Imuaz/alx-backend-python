#!/usr/bin/env python3
'''
task 1 module
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''function that reurns list of all delays'''
    delay = []

    tasks = [wait_random(max_delay) for _ in range(n)]
    result = await asyncio.gather(*tasks)

    sorted_delays = sorted(result)

    return sorted_delays
