#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that simulates a random delay.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    Asynchronously wait for a random delay.
    Returns:
        float: The actual random delay that was waited for.
    """
    random_num = random.uniform(0, max_delay)
    await asyncio.sleep(random_num)
    return random_num
