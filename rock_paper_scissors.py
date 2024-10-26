# import is a keyword for bringing in some external code that we wanna use
# random is the name of the library that has that code in it
import random

# def is a keyword for defining a function, a function is some code that when it is called
# it will execute the code inside of the definition
# play is the name of the function and the parenthesis after it signify any parameters this function will need
# to use inside the code block that is executed when the function is called
def start_the_game(): # The colon after the parenthesis just end the definition of the function signature
    # x = y is a basic variable binding, it basically just means that x now holds the value of y
    # input is a builtin function in python that will take some input from the command line, this is often called stdin (pronouced standard in)
    users_choice = input("Pick an option: 'r' for rock, 'p' for paper, 's' for scissors\n")
    # this is the choice that the computer will make again you (think chess against the computer)
    computers_choice = random.choice(['r', 'p', 's']) # choice is a function in the random library we imported, it takes a list and selects something randomly

    if users_choice == computers_choice:
        return 'it was a near win...' # This returns early from the function

    if user_wins(users_choice, computers_choice):
        return 'you win!' # This returns early from the function

    return 'you died' # This is the default if none of the other conditions are met

# The logic for determining a winner is somewhat complex because there are many different possible outcomes
# So we want to make another function that determines the winner so that our code is easier to read and reason about
def user_wins(users_choice, computers_choice):
    """returns true if the player wins"""
    # r > s, s > p, p > r
    if (users_choice == 'r' and computers_choice == 's') \
        or (users_choice == 's' and computers_choice == 'p') \
        or (users_choice == 'p' and computers_choice == 'r'):
        return True

print(start_the_game())