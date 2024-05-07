#!/usr/bin/env python3
'''Measure the runtime'''
import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measure_time: function that compute execution time
        Args:
            n(integer):number of a corotine should be run
            max_delay (integer): maximun random number
        Return(float): time it took to execute a corotine
    '''
    start = time.time()
    run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time/n
