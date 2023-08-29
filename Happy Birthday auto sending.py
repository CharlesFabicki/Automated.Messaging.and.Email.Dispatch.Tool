import smtplib as smtp
from datetime import *
import pandas as pd
from random import randint

my_email = 'username@example.com'
my_password = 'your_password_here'
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

month_day = str(datetime.now().month) + "/" + str(datetime.now().day)
data = pd.read_csv("birthdays people data.csv")
birthdays_dic = data.to_dict(orient="records")
total_birthdays = 0

for birthday in birthdays_dic:
    month_day_birth = str(birthday['month']) + "/" + str(birthday['day'])
    birthday_name = birthday['name']
    birthday_email = birthday['email']
    birthday_year = birthday['year']
    birthday_date = date(birthday_year, birthday['month'], birthday['day'])
    years = datetime.now().year - birthday_year
    random_letter = randint(1, 3)
    letter_file = f"./letter_templates/letter_{random_letter}.txt"
    if month_day == month_day_birth:
        with open(letter_file) as file:
            body = file.read()
            body = body.replace("[NAME]", birthday_name)
            body = body.replace("[YEARS]", str(years))
        with smtp.SMTP(SMTP_SERVER, PORT) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_email,
                                msg=f"Subject: Happy {years}th birthday !!\n\n{body}")
        total_birthdays += 1
    else:
        birthday = datetime(datetime.now().year, birthday_date.month, birthday_date.day)
        days = (birthday - datetime.now().today()).days + 1
        if days < 0:
            days = 365 + days
        print(f"{birthday_name}'s birthday is in {days} days ")
print(f"\n{total_birthdays} of {len(birthdays_dic)} contacts has today as birthday")
