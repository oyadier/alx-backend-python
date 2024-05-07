#!/usr/bin/env python3
'''Let's execute multiple coroutines at the same time with async'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    wait_n: Run multiple corotine at a time
        Args:
            n (integer): number of a corotine should be run
            max_delay (integer): maximun random number
        Return(List[Float]): return bedback from all corotine
    '''
    '''task1= [asyncio.create_task(wait_random(max_delay)) for _ in range(n))]'''
    result: List[float] = []
    for i in range(n):
        result.append(asyncio.create_task(wait_random(max_delay)))
    
    return [await task for task in asyncio.as_completed(result)]
