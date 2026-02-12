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


