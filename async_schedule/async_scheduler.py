"""The wrapping async classes for schedule.Job and schedule.Scheduler"""

import asyncio
from typing import Coroutine

from schedule import Job, Scheduler


class AsyncJob(Job):
    """The specialized class of the schedule.Job to be able to run
    non-async ans async functions."""

    def run(self):
        """Overloads the schedule.Job.run() with coroutine handling.

        :return: The return value returned by the `job_func`,
            or CancelJob if the job's deadline is reached.
        :rtype: Any
        """

        ret = super().run()

        if isinstance(ret, Coroutine):
            try:
                asyncio.get_running_loop()
            except RuntimeError as ex:
                if "no running event loop" in str(ex):
                    ret = asyncio.new_event_loop().run_until_complete(ret)
                else:
                    raise
            else:
                task = asyncio.create_task(ret)
                ret = asyncio.gather(task)

        return ret


class AsyncScheduler(Scheduler):
    """The specialized class of the schedule.Scheduler to be able
    to run non-async and async functions by creating AsyncJob instead
    of schedule.Job instances."""

    def every(self, interval: int = 1) -> AsyncJob:
        """Overloads the schedule.Scheduler.every() with coroutine handling
        by creating AsyncJob instead of schedule.Job instances.

        :param interval: A quantity of a certain time unit
        :return: An unconfigured :class:`AsyncJob <AsyncJob>`
        :rtype: AsyncJob
        """

        job = AsyncJob(interval, self)
        return job
