#!/usr/bin/env python3
'''Async Comprehensions '''
import asyncio
from typing import List
generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehensions"""
    return [i async for i in generator()]
