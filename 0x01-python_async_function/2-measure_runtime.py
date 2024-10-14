#!/usr/bin/env python3
"""
This module measures the runtime of the wait_n function
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """Measures the total execution time
    for wait_n and returns the average time per call."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    diff = end - start
    return diff / n
