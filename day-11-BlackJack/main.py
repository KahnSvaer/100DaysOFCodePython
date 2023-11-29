import random
import os
from art import cards, logo


def pick_card(dict_card, key):  # Why is this able to change the choice of dict_card on its own?
    """
    Inputs the cards dictionary with the key, appends a new cards for that key
    Returns if the sum greater than equal to 21, True/False to see if we can continue or not
    """
    dict_card[key].append(random.choice(cards))
    print(f"{key.capitalize()} drew {dict_card[key][-1]}")

    if check_score(dict_card[key]) > 21:
        print(f"{key.capitalize()}'s cards: {dict_card[key]} Score: {check_score(dict_card[key])}\n")
        print("BUSTED!")
        if key == "dealer":
            end("Win")
        else:
            end("Lose")
        return False
    else:
        return True


def check_score(cards_stack):  # I understand
    """
    Returns the score of the cards list
    If Ace present returns max choice under 21 or until number of ace are exhausted
    """
    if 11 not in cards_stack:
        return sum(cards_stack)
    else:
        num_ace = cards_stack.count(11)
        num_small_ace = 0
        while num_ace != num_small_ace:
            if sum(cards_stack) - num_small_ace * 10 <= 21:
                return sum(cards_stack) - num_small_ace * 10
            else:
                num_small_ace += 1
        return sum(cards_stack) - num_small_ace * 10


def game():
    """
    Main game behind the program
    """
    os.system('cls')
    print(logo)
    print("Welcome to BlackJack!\n")

    cards_list = {
        "dealer": [],
        "player": []
    }

    player = cards_list["player"]  # Why does this saves the address?
    dealer = cards_list["dealer"]

    # Game start
    pick_card(cards_list, "dealer")
    pick_card(cards_list, "player")
    pick_card(cards_list, "player")

    player_turn = True

    while player_turn:
        print(f"\nDealer's cards: {dealer} Score: {check_score(dealer)}")
        print(f"Player's cards: {player} Score: {check_score(player)}\n")

        response = False
        while not response:
            turn = input("What do you do? Type 'hit' to get new card and 'stand' to end turn: ").strip().lower()
            if turn == 'hit':
                player_turn = pick_card(cards_list, "player")
                response = True
            elif turn == 'stand':
                dealer_turn(cards_list)  # Dealer's turn from here on out
                response = True
                player_turn = False
            else:
                print("Invalid Response\n")


def dealer_turn(cards_dict):  # I Understand
    """
    This is the working behind the dealer turn
    Inputs the cards dictionary and returns nothing
    Automatically ends with the end function
    """
    print("\n")
    dealer, player = cards_dict["dealer"], cards_dict["player"]
    if pick_card(cards_dict, "dealer"):
        print(f"Dealer's cards: {dealer} Score: {check_score(dealer)}")
        if check_score(dealer) == check_score(player) and check_score(dealer) > 16:
            end("Drew")
        elif check_score(dealer) == check_score(player):
            dealer_turn(cards_dict)
        elif check_score(dealer) > check_score(player):
            end("Lose")
        else:
            dealer_turn(cards_dict)


def end(ending):  # I understand
    """
    This is used to end the program
    Customises the ending message using the inputs and returns nothing
    If correct inputs passed, restarts the game
    """
    print("\n")
    play_again = input(
        f"You {ending}! do you want to play again? Type 'y' for yes or 'n' for no ").strip().lower()
    if play_again == 'y':
        game()
    elif play_again == 'n':
        print("\nThank You for playing BlackJack!")
    else:
        print("Invalid Response!")
        end(ending)


start_game = input("do you want to play BlackJack? Type 'y' for yes or 'n' for no ").strip().lower()
if start_game == 'y':
    game()
else:
    print("Thank You for considering to play this game!")
