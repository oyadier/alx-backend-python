#!/usr/bin/python3
import asyncio 
import random
'''The basics of aysnc'''


async def wait_random(max_delay=10):
    '''
    Find random number between specified range
        Args:
            max_delay(number): maximum number of random number
            
    Return(number): the random number
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay