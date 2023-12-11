#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns (total_time / n)
    """
    stt = time.time()

    async def run_wait_n():
        await wait_n(n, max_delay)

    asyncio.run(run_wait_n())

    stp = time.time()
    return (stp - stt) / n
