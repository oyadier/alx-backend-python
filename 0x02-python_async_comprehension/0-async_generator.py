#!/usr/bin/env python3
'''Async Generator'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    async_generator: random number using yeild
        Return: yeild
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield float(uniform(0, 10))
