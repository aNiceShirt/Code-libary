import smtplib

my_email = "mathias.bhelnaes@gmail.com"
password = ""
# smtp.gmail.com
# smtplib.SMTP("smtp.gmail.com", port=587)


# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="mhelnaes@gmail.com", msg="Subject:Hello \n\n  This is the body of my email")
# connection.close()


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="mhelnaes@gmail.com", 
#                         msg="Subject:Hello \n\n  This is the body of my email")

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1994, month=3, day=7)


import random
import datetime as dt

quotes = open("day-32_email/quotes.txt", "r")

list_quotes = quotes.readlines()
list_quotes = [quote[:-1] for quote in list_quotes]

quote =random.choice(list_quotes)

quote = quote.replace("\\", "")

print(quote)

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="mhelnaes@gmail.com", 
                            msg="Subject:Monday inspirational quote \n\n "+ quote)