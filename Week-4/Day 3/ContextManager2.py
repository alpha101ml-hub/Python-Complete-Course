import time 

class TimeIt:
    def __enter__(self):
        self.start_time = time.perf_counter()  # Start the clock
        return self  # This allows you to assign it to a variable if needed
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()  # Stop the clock
        elapsed_time = self.end_time - self.start_time  # Calculate elapsed time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")  # Print the elapsed time
        
# Example usage
with TimeIt():
    million_number = sum(i * 2 for i in range(1_000_000))