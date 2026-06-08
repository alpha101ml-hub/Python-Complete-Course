# Day 1 - Lists (indexing, slicing, methods)
fruit = ["apple", "banana", "cherry"]
print(fruit[0])     # apple
print(fruit[-1])    # cherry
fruit.append("orange")
fruit.insert(1, "blueberry")
fruit.remove("banana")
print(fruit)  #['apple', 'blueberry','cherry','orange']

# Exercise. 
# Create a list of 5 numbers. Print the first, third and last element. Then add a new number at the end and remove the second element.

num = [1,2,3,4,5]
print(num[0])
print(num[2])
print(num[-1])

num.append(6)
num.remove(2)
print(num)