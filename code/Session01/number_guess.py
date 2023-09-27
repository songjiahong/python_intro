import random

print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 20.")

number = random.randint(1, 20)

while True:
    guess = int(input("Your guess: "))
    if guess == number:
        print("Bingo! You guessed it!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")