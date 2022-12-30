# Async Schedule

async_schedule Module

Extension of the python schedule module (https://schedule.readthedocs.io/en/stable/) with the ability to handle asyncio coroutines / calling async functions.

Usage
-----
```python
import asyncio
import time

from async_schedule import schedule


# function
def foo():
    print("foo")


# coroutine function
async def bar():
    print("bar")


# enqueue function in scheduler
schedule.every().second.do(foo)

# enqueue coroutine function in scheduler
schedule.every(2).seconds.do(bar)  # no call of coroutine function here, just add the coroutine function


# synchronous way shall work as expected from schedule module
while True:
    schedule.run_pending()
    time.sleep(1)


# run within running asyncio loop by enqueuing schedule.run_pending in the running loop
async def main():
    loop = asyncio.get_running_loop()

    while True:
        loop.call_soon(schedule.run_pending)
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
```
