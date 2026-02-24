def decision(choice: str) -> int:
    """
    This looks at what the user entered and returns a code.
    """
    if choice == "y":
        return 1
    elif choice == "n":
        return -1
    else:
        return 0


while True:
    selection = input("What is your choice: y or n?").strip().lower()
    code = decision(selection)

    if code == 1:
        print("You answered YES")
        break
    elif code == -1:
        print("you answered NO")
    else:
        print("you did not answer y or n. Try again!")
