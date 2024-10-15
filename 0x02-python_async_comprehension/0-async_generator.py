#!/usr/bin/env python3
"""
This script demonstrates the use of an asynchronous generator
that yields random floating-point numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields 10 random float values.
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
