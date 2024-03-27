import datetime as dt
import random
import smtplib

email = ""  # Enter your email here
disposable_email = ""  # Enter some sort of disposable email here
password = ""  # Enter your password here

now = dt.datetime.now()


def send_message(quote):
    message = f"Subject:Monday Motivation\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email, to_addrs=disposable_email, msg=message)


if now.weekday() == 0:  # Monday
    try:
        with open("quotes.txt") as file:
            data = file.readlines()
    except FileNotFoundError:
        print("No file Found")
    else:
        random_quote = random.choice(data).strip()
        send_message(random_quote)
else:
    print("Not today")
