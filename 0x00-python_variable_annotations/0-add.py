#!/usr/bin/env python3

"""
Type annotated function
"""


def add(a: float, b: float) -> float:
    """
    Adds 2 numbers and returns their sum.

    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The sum of `a` and `b`.
    """
    return a + b
