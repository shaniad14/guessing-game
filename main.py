"""
Number Guessing Game (Simple Version)
"""

import random


# get a valid number
def get_number(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a number.")


# get y or n only
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y" or answer == "n":
            return answer
        print("Enter only y or n.")


# play one game
def play():
    print("\n--- New Game ---")

    low = get_number("Low number: ")
    high = get_number("High number: ")

    # make sure high is bigger
    while high <= low:
        print("High must be greater than low.")
        high = get_number("High number: ")

    attempts = get_number("Number of guesses: ")
    secret = random.randint(low, high)

    used = 0

    while used < attempts:
        guess = get_number("Your guess: ")
        used += 1

        if guess == secret:
            print(f"You win in {used} guesses!")
            return
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

        print("Guesses left:", attempts - used)

    print("You lost. The number was", secret)


# main program
name = input("What is your name? ").strip()
print("Hello", name)

while True:
    play()
    again = get_yes_no("Play again? (y/n): ")
    if again == "n":
        print("Goodbye!")
        break
