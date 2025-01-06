import timeit

code_to_measure = """
import numpy as np

def find_even_numbers(start, stop):
    if start % 2 == 0:
        return np.arange(start, stop, 2)
    else:
        return np.arange(start + 1, stop, 2)

result = find_even_numbers(0, 1000000000)
"""


execution_time = timeit.timeit(code_to_measure, number=1)

print("Execution time:", execution_time, "seconds")
