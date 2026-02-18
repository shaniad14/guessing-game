"""
NUMBER GUESSING GAME
"""

import random


# safe number input
def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Enter a valid number.")


# play one round
def play():

    low = get_number("Minimum number: ")
    high = get_number("Maximum number: ")

    secret = random.randint(low, high)
    attempts = get_number("How many guesses? ")

    print("\nGuess the number!")

    while attempts > 0:

        guess = get_number("Your guess: ")

        if guess == secret:
            print("You win!")
            return

        elif guess < secret:
            print("Too low!")

        else:
            print("Too high!")

        attempts -= 1
        print("Guesses left:", attempts)

    print("You lost! The number was:", secret)


# main loop
while True:

    play()

    again = input("\nPlay again? (y/n): ").lower()

    if again == "n":
        print("Goodbye!")
        break
