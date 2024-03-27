import random
import smtplib

import pandas
import datetime as dt
import os

EMAIL = ""  # Enter your gmail here
PASSWORD = ""  # Enter your password here

now = dt.datetime.now()

bday_data = pandas.read_csv("birthdays.csv")
bday_today = bday_data[(bday_data["month"] == now.month) & (bday_data["day"] == now.day)]

root = "letter_templates"
letters = [letter for _, _, letter in os.walk(root, topdown=True)][0]
if not len(letters):
    raise FileNotFoundError
letters = [os.path.join(root, letter) for letter in letters]


def get_random_letters():
    random_temp = random.choice(letters)
    with open(random_temp) as file:
        data = file.read()
    return data


def send(rec_email, text):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=rec_email, msg=f"SUBJECT:Happy Birthday!!\n\n{text}")


def send_email(bday_row):
    template = get_random_letters()
    name = bday_row["name"]
    template = template.replace("[NAME]", name)
    email = bday_row["email"]
    send(email, template)


[send_email(row) for index, row in bday_today.iterrows()]
