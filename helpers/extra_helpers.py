import random
import string
import time


def random_ascii_string(length: int = 8) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def waiter(func, *args, retry_exception, seconds: int = 10, **kwargs):
    retry = 0

    while retry < seconds:
        try:
            return func(*args, **kwargs)
        except retry_exception:
            time.sleep(1)
            retry += 1
