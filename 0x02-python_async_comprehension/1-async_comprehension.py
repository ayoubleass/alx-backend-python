#!/usr/bin/env python3
"""
Coroutine to collect random numbers using async comprehension.
"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collects 10 random numbers using async comprehension over async_generator.
    """
    return [num async for num in async_generator()]
