# Basic Input and Output
print("Hello", "world", sep="-", end="!\n")

# Input wit input(always returns a string)
name = input("What is your name? ")
print("Nice to meet you,",name)

#Converting types:
age_str = input("Age: ")
age = int(age_str)  # convert string to int

# Ask user for two numbers, convert to integer, print their sum
n1 = input("What is the first number? ")
n2 = input("What is the second number? ")

print(int(n1)+ int(n2))