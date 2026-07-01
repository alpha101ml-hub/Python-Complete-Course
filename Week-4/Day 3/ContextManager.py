# Exercise
# Write a context manager that measures the time a block of code takes to run. Print the elapsed time after exiting.

import time
from contextlib import contextmanager

@contextmanager
def time_it():
    start_time = time.perf_counter()  # 1. Start the clock
    try:
        yield # 2. Hand control over to the block of code inside "with"
    finally:
        end_time = time.perf_counter()  # 3. Stop the clock
        elapsed_time = end_time - start_time  # 4. Calculate elapsed time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")  # 5. Print the elapsed time
        
# Example usage
with time_it():
    million_number = [i * 2 for i in range(1_000_000)]