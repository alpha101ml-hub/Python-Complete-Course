# Ask for a number. Print "Positive" "negative" or "zero"
num = int(input("Enter a number: "))

if (num>0):
    print("Positive")
elif (num<0):
    print("Negative")
else:
    print("Zero")
    
# Keep asking the fornpassword until the enter "python123". Print "Access granted" when correct
password = input("Enter a password: ")
while (password != "python123"):
       print("Please Try again")
       password = input("Enter a password: ")
print("Access granted")

       
# Use a for loop to print all even numbers from 2 to 20
for i in range(2,21):
    if(i%2==0):
        print(i)
        
# Ask for a number n, then use a loop to print the multiplication table of n (1 to 10).
n = int(input("Enter a number: "))
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
    
    
# Enhance the game: limit attempts to 7, tell the user when they run out

import random
secret = random.randint(1, 100)
guess = None
attempt = 0
max_attempts = 7

while attempt < max_attempts:
    guess = int(input(f"Attempt {attempt+1}/{max_attempts} - Guess a number between 1 and 100: "))
    attempt += 1
    if guess == secret:
        print(f"Correct! It took you {attempt} attempts.")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")
    
    if attempt == max_attempts and guess != secret:
        print(f"Sorry, you ran out of attempts. The secret number was {secret}.")