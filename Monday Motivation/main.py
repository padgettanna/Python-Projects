import datetime as dt
import smtplib
import random

my_email = "your email address here"
password = "your password"
day_of_week = dt.datetime.now().weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quotes = quotes.readlines()
        random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="recepients email address",
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")
