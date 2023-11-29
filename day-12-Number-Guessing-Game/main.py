from random import randint
from art import logo
from os import system


def game():
    system("cls")

    random_num = randint(1, 100)

    print(logo)
    print("Welcome to the number guessing game!\n")

    response = False
    lives = 0

    while not response:
        mode = input("Enter the mode1 that you want to play\nType 'h' for hard mode and 'e' for easy! ").strip().lower()
        if mode == 'e':
            lives = 10
            response = True
        elif mode == 'h':
            lives = 5
            response = True
        else:
            print("Invalid Input\n")

    in_game = True
    while in_game:
        print(f"\n\n{lives} lives left!")

        if lives == 0:
            in_game = False
            end("l",random_num)

        guess = int(input("Enter your guess: "))

        if guess > random_num:
            print("Too high")
            lives -= 1
        elif guess < random_num:
            print("Too low")
            lives -= 1
        else:
            in_game = False
            end("w",random_num)


def end(mode,random_num):
    """
    The ending sequence for the game
    mode1 allowed "w" or "l"
    """
    print(f"The number was {random_num}.")
    if mode == "l":
        print("All lives are lost. You LOSE!")
    else:
        print("You guessed the number correctly. You WIN!")
    response = False
    while not response:
        mode = input("\nDo you want to play again?\nType 'y' for yes and 'n' for no! ").strip().lower()
        if mode == 'y':
            response = True
            game()
        elif mode == 'n':
            response = True
            print("Thank you for playing!")
        else:
            print("Invalid Input")


response1 = False
while not response1:
    mode1 = input("\nDo you want to play This game?\nType 'y' for yes and 'n' for no! ").strip().lower()
    if mode1 == 'y':
        response1 = True
        game()
    elif mode1 == 'n':
        response1 = True
        print("Thank You for considering this game!")
    else:
        print("Invalid Input")
