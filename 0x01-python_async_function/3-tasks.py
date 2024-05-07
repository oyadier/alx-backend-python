#!/usr/bin/env python3
'''The basics of aysnc'''
import asyncio
from asyncio import Task
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    wait_random: Find random number between specified range
        Args:
            max_delay(integer): maximum number of random number

        Return (task): asyncio task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
