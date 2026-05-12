# Simple Calculator
# Write a script
# 1. Ask for two number
# 2. Ask for an opertor (+,-,*,/)
n1 = float(input("What is the first number? "))
n2 = float(input("What is the second number? "))
op = input("Operation (+,-,*,/): ")

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    result = n1 / n2
else:
    result = "Invalid operation"
    
print("Result:", result)


