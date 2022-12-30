# Async Schedule

async_schedule Module

Extension of the python schedule module (https://schedule.readthedocs.io/en/stable/) with the ability to handle asyncio coroutines / calling async functions.

Usage
-----
The async_schedule Module will work as expected from schedule module, like:

```python
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

Furthermore, we will be able to enqueue coroutine functions (also a mixed set of functions / coroutine functions) like in the examples below:

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
