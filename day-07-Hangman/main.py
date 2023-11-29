import random
import art
import wordlist
import os

stages = art.stages
word_list = wordlist.word_list
lives = 6

inGame = True

selected_word = random.choice(word_list).lower()
guess_result = list("_" * len(selected_word))
guess_list = []
print(art.logo)

while inGame:
    print(stages[lives])
    print(guess_result)
    guess = input("Enter a letter\t").strip().lower()
    os.system('cls')

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input")
    else:
        print(f"You have guessed {guess} as the letter")
        if guess in guess_list:
            print("You have already guessed this before")

        else:
            guess_list.append(guess)
            if guess not in selected_word:
                print("Unfortunately, you have chosen the wrong letter!")
                lives -= 1
            else:
                print("You have guessed correctly!")
                for i in range(len(selected_word)):
                    if guess == selected_word[i]:
                        guess_result[i] = guess

    if "_" not in guess_result:
        inGame = False
        print(stages[lives])
        print(guess_result)
        print("You Win!:)")
    if lives == 0:
        inGame = False
        print(stages[lives])
        print(guess_result)
        print(f"This word was {selected_word}")
        print("You Lose!:(")
