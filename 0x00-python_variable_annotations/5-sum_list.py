#!/usr/bin/env python3
'''Sum up the all float elem of a list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list: Add elements of a list params
        input_list(list): list containing float types

    Return (float): sum of all the elements in the list
    """
    return sum(input_list)
