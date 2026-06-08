# Day 3 - Dictionaries (key-value pairs)
person = {
    "name": "Alice",
    "age": 25,
    "city": "Jaipur"
}
print(person["name"])
person["age"] = 26
person["job"] = "Engineer"  # add new key

# Exercise.
# Create a dictionary that maps 3 student names to their grades. Ask the user for a name, then print that student's grade.
grades = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
print("Enter a student's name:")
name = input()
print(grades[name])