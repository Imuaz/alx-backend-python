#!/usr/bin/env python3
'''
Measure run time module
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' function measures the total runtime and returns it.'''
    tasks = [async_comprehension() for _ in range(4)]

    start_time = time.time()

    await asyncio.gather(*tasks)

    end_time = time.time()

    total_runtime = end_time - start_time

    return total_runtime
