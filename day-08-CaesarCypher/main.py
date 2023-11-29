import extras

logo_cypher = extras.logo
alphabet = extras.alphabet


def caesar(start_text, shifted_amount, cypher_direction):
    end_text = ""
    if cypher_direction == 'encode':
        direction_const = 1
    elif cypher_direction == 'decode':
        direction_const = -1
    else:
        print("Invalid Inputs")
        return
    for char in start_text:
        if char in alphabet:
            position_old = alphabet.index(char)
            position_new = (position_old + direction_const * shifted_amount) % len(alphabet)
            end_text += alphabet[position_new]
        else:
            end_text += char
    print(f"The {cypher_direction}d text is {end_text}.")


print(logo_cypher)
in_game = True

while in_game:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shifted_amount number:\n"))

    caesar(text, shift, direction)

    result = input("Do you want to use this again? Type y for yes and n for no\n").strip().lower()

    if result == 'n':
        in_game = False
        print("GoodBye!")
