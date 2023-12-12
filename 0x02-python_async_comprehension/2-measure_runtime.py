#!/usr/bin/env python3
"""
write a measure_runtime coroutine that will execute async_comprehension four
times in parallel using asyncio.gather.
"""
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime should measure the total runtime and return it.
    """
    stt = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    stp = asyncio.get_event_loop().time()
    return (stp - stt)
