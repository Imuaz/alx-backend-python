#!/usr/bin/env python3
'''
task 2 module
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_dey: int) -> float:
    """Measure and return the average execution time per call to wait_n."""
    r_time: float = time.time()
    asyncio.run(wait_n(n, max_dey))
    r_time = time.time() - r_time

    return r_time / n
