import random

number = random.randint(1, 50)
attempts = 0
guess = 0

while guess != number:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print(f"Correct! You guessed it in {attempts} attempts")
