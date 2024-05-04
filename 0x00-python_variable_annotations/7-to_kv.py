#!/usr/bin/python3
'''String and int/float to tuple'''
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple:
    '''
    to_kv: for a tuple
        Args:
          k  (string): the key to the tuple value
          v (float, float): key's value
    Return: a tuple'''

    return (k, (v ** 2))
