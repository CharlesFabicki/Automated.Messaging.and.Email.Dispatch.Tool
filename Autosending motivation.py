# Auto sending motivation code to your friends

import random
import datetime as dt
import smtplib

my_email = 'pythontstng@gmail.com'
my_password = 'ipenpekqatkwhlbz'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == now.weekday():
    with open("quotes for motivation script.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()  # to encrypt email
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='biyof42822@touchend.com',
            msg=f"Subject:Every Day Motivation\n\n{quote}"
        )

#  !!!!!!  to_addrs='biyof42822@touchend.com'  You can generate your own disposable emial using: https://temp-mail.org/en/