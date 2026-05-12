#Day 1 - Print a trangle using three print lines:
print("*")
print("**")
print("***")

# Day 2 - Swap two varaiable withous using a third varable (use tuple unpacking: a, b = b,a)
a1 = "String"
b1 = "Ring"
a1, b1 = b1, a1
print(a1)
print(b1)

# Day 3 - Ask for a person's first name and last name separately, then print "Last, First".
firstname = input("Please tell your first name: ")
secondname = input("Please tell your last name: ")
print(secondname, firstname)

# Day 4 - Given a temperature in Celsius (user input), convert to Fahrenheit:
# F = C * 9/5 + 32
temp = input("What is the temparature in Celcius: ")
print(temp + " Celcius")
# print(int(temp) * 9/5 + 32)
print(str(int(temp) * 9/5 + 32) + " Fahrenheit")

# Day 5 - Write a tip calculator - ask for bill total, percentage, number of people - output tip per person and total per person
n1 = float(input("What is the bill total? "))
n2 = float(input("How much like you to tip: 5% , 10% or 15%: "))
n3 = int(input("How many people are there: "))

tip_amount = n1 * (n2/100)
total_with_tip = n1 + n2
total_per_person = total_with_tip / n3

print(f"Tip per person: {tip_amount / n3:.2f}")
print(f"Total per person: {total_per_person:.2f}")