with open("Input/Names/invited_names.txt") as name_file:
    recipients = list(map(str.strip, name_file.readlines()))

with open("Input/Letters/starting_letter.txt") as file:
    content = file.read()

for recipient in recipients:
    new_content = content.replace("[name]", f"{recipient}")
    with open(f"Output/ReadyToSend/letter_for_{recipient}.txt", mode="w") as output:
        output.write(new_content)
