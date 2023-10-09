#!/usr/bin/env python3
'''
task 2 module
'''
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_dey: int) -> float:
    """Measure and return the average execution time per call to wait_n."""
    total_time = 0.0

    for _ in range(n):
        start_time = time.time()
        asyncio.run(wait_n(1, max_dey))  
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        total_time += elapsed_time

    average_time_per_call = total_time / n

    return average_time_per_call
