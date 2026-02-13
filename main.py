# Import random module
import random


# Function to safely get a number from the user
def get_number(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except:
            print("Please enter a valid number.")


# Function to get only y or n
def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == "y" or answer == "n":
            return answer
        print("Enter only y or n.")


# Function to play one round
def play_game(name):

    print("\nLet's set up your game,", name)

    # Ask for range
    while True:
        low = get_number("Low number: ")
        high = get_number("High number: ")

        if high > low:
            break
        print("High must be greater than low.")

    # Ask for attempts
    attempts = get_number("How many attempts? ")

    # Generate random number
    secret = random.randint(low, high)

    used = 0

    print(f"\nGuess a number between {low} and {high}")

    # Guess loop
    while used < attempts:
        guess = get_number("Your guess: ")
        used += 1

        if guess == secret:
            print("Correct! You won!")
            return

        if guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        print("Attempts left:", attempts - used)

        print("Attempts left:", attempts - used)

    # If they lose
    print("Out of tries!! The number was", secret)


# Main game loop
def main():

    name = input("Enter your name: ").strip()
    print("Welcome,", name)

    while True:
        play_game(name)

        again = get_yes_no("\nPlay again? (y/n): ")
        if again == "n":
            print("Goodbye!")
            break


# Start the game
main()
