# Day 2 - Custom Exceptions & Raising Errors

class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("No negative numbers allowed")
    raise n ** 0.5

try:
    print((square_root(-4)))
except NegativeNumberError as e:
    print(e)
    
    
# Create a validate_age(age) function that raises a ValueError if age < 0 or age > 150. Call it in a loop until valid input is given.
def valid_age(age):
    if age < 0:
        raise valid_age("less than 0 is not allowed")
    elif 0 < age and age > 150:
        print(f"you are {age} years old") 
    
        
try:
    print(valid_age(0))
except valid_age as err:
    print(err)