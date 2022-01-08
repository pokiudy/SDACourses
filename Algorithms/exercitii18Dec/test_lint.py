"""
This is the Time module
"""

import time


class TimerDecorator:
    """
    Docstring class
    """

    def __init__(self, func):
        self.times = []
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        delta_time = time.time() - start_time
        self.times.append(delta_time)
        print(f"Function {self.func.__name__} has been executed in {delta_time}s "
              f"with the following arguments: {args} {kwargs}")
        return result

    @staticmethod
    def random_method():
        """
        docstring
        :return:
        """
        print("We are good!")


@TimerDecorator

def calculate_product_a_million_times(small_number):
    """
    doc for method
    """

    for _ in range(1_000_000):
        large_number = 4**39
        _ = large_number * small_number + small_number ** 39


if __name__ == "__main__":
    calculate_product_a_million_times(10)
