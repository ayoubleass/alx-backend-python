#!/usr/bin/env python3
"""
This module provides a function to create a task for wait_random.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """
    Creates an asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))
