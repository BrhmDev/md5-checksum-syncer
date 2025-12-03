import time
from typing import Callable

class Task:
    session = None,


def schedule_interval(func: Callable, interval_minutes: int):
    while True:
        func()
        time.sleep(interval_minutes * 60)
