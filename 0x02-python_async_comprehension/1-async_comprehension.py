#!/usr/bin/env python3
"""
Async comprehensions
"""
from typing import List
import asyncio
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehension over async_generator
    then return 10 random numbers.
    """
    return [i async for i in async_generator()]
