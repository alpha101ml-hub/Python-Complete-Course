'''
📚 Novice Stage – Week 2: Control Flow

Now that you can work with variables, input/output, and basic math, it’s time to learn how to make decisions and repeat actions.
Day 1 – if, elif, else (review + deeper)

Already used in calculator, but let's add comparisons (==, !=, <, >, <=, >=).

Example: Grade calculator
'''
score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is", grade)