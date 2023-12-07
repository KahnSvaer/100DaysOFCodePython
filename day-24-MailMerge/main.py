LETTER_STARTER_PATH = "./Input/Letters/starting_letter.txt"
NAMES_PATH = "./Input/Names/invited_names.txt"
OUTPUT_PATH = "./Output/ReadyToSend/"

with open(LETTER_STARTER_PATH) as starter:
    starter_Letter = starter.read()

with open(NAMES_PATH) as names_file:
    names = names_file.read().strip().split("\n")

for name in names:
    with open(OUTPUT_PATH+f"letter_for_{name}.txt", mode="w") as letter:
        letter.write(starter_Letter.replace("[name]", f"{name}"))



