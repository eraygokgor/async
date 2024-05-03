import time
import numpy as np


def function_timer(func):
    """
    Decorator to run a function multiple times and get the mean result of the executions.
    :param func: Function to decorate.
    :return: Decorator function.
    """
    def wrapper(*args, n=1, **kwargs):
        results = []
        for _ in range(n):
            start = time.time()
            result = func(*args, **kwargs)
            results.append(time.time() - start)
        mean_time = np.mean(results)
        std_dev = np.std(results)
        print(f'Mean time for {n} runs: {round(mean_time, 2)} ± {round(std_dev, 2)} seconds.')
        return result
    return wrapper
