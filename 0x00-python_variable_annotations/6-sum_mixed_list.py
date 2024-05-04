#!/usr/bin/env python3
'''Add sum of mixed elem types'''
from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """
    Function to add all diff type of list elements
        Args:
            mxd_lst (int, float): int and float elements

        Return (float): a sum of all element
    """
    return sum(mxd_lst)
