import time
from typing import Callable
import logging


def schedule_interval(func: Callable, interval_minutes: int):
    while True:
        try:
            func()
        except Exception as e:
            logging.error(f"Exception thrown while executing task: {e}")
        time.sleep(interval_minutes * 60)
