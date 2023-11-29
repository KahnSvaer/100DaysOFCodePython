import random
from os import system
from art import logo, vs
from game_data import data


def compare(A, B):
    """
    Useful for comparisons
    """
    if A['follower_count'] > B['follower_count']:
        return -1
    elif A['follower_count'] < B['follower_count']:
        return 1
    else:
        return 0


def to_continue(A, B):
    """
    Mixture of asking input and Checking the correctness
    """
    response = 0
    is_correct_inputs = False
    while not is_correct_inputs:
        guess = input("Which is higher; A or B? ").strip().lower()
        if guess == 'a':
            is_correct_inputs = True
            response = -1
        elif guess == 'b':
            is_correct_inputs = True
            response = 1
        else:
            print("Invalid Inputs\n")
    if response * compare(A, B) >= 0:
        return True
    else:
        return False


def format_data(dict):
    print(f"Compare A: {dict['name']}, a {dict['description']}, from {dict['country']}")


def intro(A, B):
    """
    An introductory function to create the starting portion of the code
    Formats the chosen elements and prints the logo
    """
    system('cls')
    print(logo)
    format_data(A)
    # print(A)
    print(vs)
    format_data(B)
    # print(B)


def game():
    first_element = random.choice(data)
    in_game = True
    score = -1
    while in_game:
        score += 1
        second_element = random.choice(data)
        intro(first_element, second_element)
        print(f"Currant Score: {score}")
        in_game = to_continue(first_element, second_element)
        first_element = second_element
    end(score)


def end(score):
    print(f"\nYour final score is {score}")
    val2 = False
    while not val2:
        result = input("Do you want to play this game again? Type 'y for yes and 'n' for no ").strip().lower()
        if result == 'y':
            game()
        elif result == 'n':
            print("Thank you for playing this game!")
        else:
            print("Invalid Inputs\n")


val = False
print(logo)
while not val:
    guess1 = input("Do you want to play this game? Type 'y for yes and 'n' for no\n").strip().lower()
    if guess1 == 'y':
        game()
    elif guess1 == 'n':
        print("Thank you for considering to play this game!")
    else:
        print("Invalid Inputs\n")
