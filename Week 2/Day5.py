# Day 5 – Mini Project: Number Guessing Game

# Combine everything: random number, loop, conditions.

import random
secret = random.randint(1,100)
guess = None
attempt = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 100: "))   
    attempt += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"Correct! It took you {attempt} attempts.")