import smtplib

my_email = ""  # Enter your email here
disposable_email = ""  # Enter some sort of disposable email here
password = ""  # Enter your password here

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=disposable_email, msg="Subject:Hello!\n\nThis is the body of the msg.+")
connection.close()
