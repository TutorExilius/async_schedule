import schedule as schedule

from async_schedule.async_scheduler import AsyncScheduler

schedule.default_scheduler = AsyncScheduler()
