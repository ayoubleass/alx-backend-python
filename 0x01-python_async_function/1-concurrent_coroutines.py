#!/usr/bin/env python3
"""
This module contains asynchronous routines to wait for random delays.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    delays = [await task for task in tasks]
    return delays
