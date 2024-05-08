#!/usr/bin/env python3
'''Run time for four parallel comprehensions'''
import asyncio
import time
async_com = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime: measure run parallet comprehension
        Return(float): run time"""
    start = asyncio.get_event_loop().time()
    '''Using unpacking generator comprehension'''
    await asyncio.gather(*(async_com() for _ in range(4)))
    end = asyncio.get_event_loop().time()
    run_time = end - start
    return run_time
