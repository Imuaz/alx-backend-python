#!/usr/bin/env python3
'''
task 2 module
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure and return the average execution time per call to wait_n."""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    average_time = end_time - start_time
    
    return average_time / n
