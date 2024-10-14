#!/usr/bin/env python3
"""
This module contains asynchronous routines to wait for random delays.
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n, max_delay):
    """
    Spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    tasks = asyncio.as_completed(tasks)
    delays = [await task for task in tasks]
    return delays
