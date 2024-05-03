import time


def function_timer(func: callable) -> callable:
    """
    Decorator to measure the time a function takes to execute.
    :param func: Function to measure the time it takes to execute.
    :return: Wrapper function that measures the time the function takes to execute.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Executed in {round(time.time() - start, 2)} seconds.')
        return result
    return wrapper
