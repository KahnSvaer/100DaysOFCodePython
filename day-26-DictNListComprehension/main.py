import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {rows.letter: rows.code for (index, rows) in nato_data.iterrows()}


def generate_phonetic():
    try:
        check_string = input("Enter a string: ").strip().upper()
        string_list = [nato_dict[letter] for letter in check_string]
        print(string_list)
    except KeyError:
        print("Sorry only letters please\n")
        generate_phonetic()


generate_phonetic()
