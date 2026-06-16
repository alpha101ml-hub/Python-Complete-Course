'''
📚 Novice Stage - Week 4: Error Handling, Files, Context Managers
'''

try:
    num = int(input("Enter a number: "))
    result = 100/num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"Result: {result}")  # runs only if no exception
finally:
    print("Execution done.")  # always runs
    
    
'''
Write a program that asks for two numbers and divides them. Handle ValueError, ZeroDivisionError, and print a friendly message for each.
'''


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    results = num1/num2
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"Result: {results}")  # runs only if no exception
finally:
    print("Execution done.")  # always runs