import random
import string
import time


def random_ascii_string(length: int = 8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def waiter(func, *args, seconds: int = 10, **kwargs):
    retry = 0

    while retry < seconds:
        result = func(*args, **kwargs)
        if result is not None and not isinstance(result, Exception) and result != b'':
            return result

        time.sleep(1)
        retry += 1
