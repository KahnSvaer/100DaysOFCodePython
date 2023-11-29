from random import randint

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

rps_array = [rock, paper, scissor]

computer_choice = randint(0, 2)
user_choice = (input("Enter 0 for Rock, 1 for Paper, 2 for Scissor "))

if user_choice not in ["0", "1", "2"]:
    print("Invalid Choice You Lose!")
else:
    user_choice = int(user_choice)
    print("Your choice:")
    print(rps_array[user_choice])

    print("Computer's choice:")
    print(rps_array[computer_choice])

    if user_choice < computer_choice or (user_choice == 2 and computer_choice == 0):
        print("You Lose!")
    elif user_choice == computer_choice:
        print("Draw!")
    else:
        print("You Win!")
