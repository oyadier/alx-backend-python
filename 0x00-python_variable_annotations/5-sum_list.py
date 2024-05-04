#!/usr/bin/env python3
'''Sum up the all float elem of a list'''


def sum_list(input_list: list[float]) -> float:
    """
    sum_list: Add elements of a list params
        input_list(list): list containing float types

    Return (float): sum of all the elements in the list
    """
    sum: float = 0
    for f in input_list:
        sum += f
    return sum
