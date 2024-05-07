#!/usr/bin/env python3
'''Async Generator'''
import asyncio
from random import uniform


async def async_generator():
    '''
    async_generator: return random number using yeild
        Return: yoild
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
