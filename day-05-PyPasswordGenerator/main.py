import random

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters do you want in your password?\t"))
num_symbols = int(input("How many symbols do you want in your password??\t"))
num_numbers = int(input("How many numbers do you want in your password??\t"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

unshuffled_password = []
shuffled_password = []
password = ""

unshuffled_password.extend(random.choices(letters, k=num_letters))
unshuffled_password.extend(random.choices(numbers, k=num_symbols))
unshuffled_password.extend(random.choices(symbols, k=num_numbers))

random.shuffle(unshuffled_password)

for index in range(num_numbers+num_symbols+num_letters):
    element = random.choice(unshuffled_password)
    shuffled_password.append(element)
    unshuffled_password.remove(element)

for str in shuffled_password:
    password += str

print(f"Here's your password: {password}")
