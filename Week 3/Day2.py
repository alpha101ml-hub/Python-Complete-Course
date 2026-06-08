# Day 2 - List operations & loops
numbers = [1,2,3,4,5]
print(sum(numbers))   # 15
print(max(numbers))   # 5
print(min(numbers))   # 1
print(len(numbers))   # 5
square = [x**2 for x in numbers]  # list comprehension (preview)
print(square)  # [1, 4, 9, 16, 25]

# Exercise.
# Ask the user for 5 numbers, store them in a list, then print the average (sum/length)

num = []
for i in range(5):
    num.append(int(input("Enter a number: ")))
    
average = sum(num) / len(num)
print(average)