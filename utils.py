import time


def function_timer(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Executed in {round(time.time() - start, 2)} seconds.')
        return result
    return wrapper
