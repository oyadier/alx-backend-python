#!/usr/bin/python3
'''The basics of aysnc'''
import asyncio
import random


async def wait_random(max_delay=10):
    '''
    Find random number between specified range
        Args:
            max_delay(integer): maximum number of random number

        Return(integer): the random number
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
