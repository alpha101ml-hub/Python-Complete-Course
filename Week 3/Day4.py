# Day 4 - Tuples (immutable) & Sets (unique, unordered)

# Tuple - cannot change
coordinates = (10, 20)
x, y = coordinates  # unpacking

# Set - no duplicates
colors = {"red", "green", "blue"}
colors.add("red")  # nothing changes
colors.add("yellow") 
print(colors)  # {'red', 'green', 'blue', 'yellow'}

# Exercise.
# Create a list with duplicate numbers, then convert it to a set to remove duplicates. Print both the original list and the set.
num = [1,2,3,4,4,3,2,1]
num_set = set(num)
print("Original list:", num)
print("Set (duplicates removed):", num_set)