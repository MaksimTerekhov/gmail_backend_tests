import time


def waiter(func, *args, retry_exception, seconds: int = 10, **kwargs):
    retry = 0

    while retry < seconds:
        try:
            return func(*args, **kwargs)
        except retry_exception:
            time.sleep(1)
            retry += 1
