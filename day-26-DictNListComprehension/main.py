import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {rows.letter: rows.code for (index, rows) in nato_data.iterrows()}

check_string = input().strip()
string_list = [nato_dict[letter.upper()] for letter in check_string if letter.isalpha()]
print(string_list)