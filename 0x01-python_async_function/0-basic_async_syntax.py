#!/usr/bin/env python3
'''
task 0 module
'''
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    '''function that takes returns a random delay b/w in argument'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
