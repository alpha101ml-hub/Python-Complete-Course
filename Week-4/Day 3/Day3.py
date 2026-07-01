# using contextlib

from contextlib import contextmanager

@contextmanager
def managed_file(filename):
    f = open(filename, "w")
    try:
        yield f
    finally:
        f.close()
        
with managed_file("test.txt") as f:
    f.write("Hello")
    
    