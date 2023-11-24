import random

max_number = random.randint(1, 99)

print("Welcome to Guess the Number!")
print(f"I'm thinking of a number between 1 and {max_number}.")

number = random.randint(1, max_number)

while True:
    guess = int(input("Your guess: "))
    if guess == number:
        print("Bingo! You guessed it!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")