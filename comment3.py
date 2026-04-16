import random  

secret = random.randint(1, 10)  
attempts = 0  

print("Guess a number between 1 and 10")  

while True:  
    guess = int(input("Enter your guess: "))  
    attempts += 1  

    if guess == secret:  
        print("Correct!")  
        break  
    elif guess < secret:  
        print("Too low!")  
    else:  # too high
        print("Too high!")  

print("Attempts taken:", attempts)  
