# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.
import sys

points = 5
numbers = set()

while True:
    ans = input("Please input a number: ")
    # Use exception handling to check for integer.
    try:
        int(ans)
    except ValueError:
        print("That's not a valid answer.", end=" ")
        continue
    # Subtract point if answer in numbers. Otherwise, add to the list and check if list is greater than 10 items.
    if ans in numbers:
        print("You've already tried that number. You lose a point.")
        points -= 1
        if points == 0:
            print("Sorry, you lose.")
            sys.exit()
        else:
            continue
    else:
        print("The number has been added to the list.")
        numbers.add(ans)
        if len(numbers) > 10:
            print("Congratulations! You win!")
            sys.exit()
        else:
            continue

