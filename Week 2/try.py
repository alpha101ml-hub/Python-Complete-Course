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