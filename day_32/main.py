# import smtplib
#
# my_email = "gakurufam@gmail.com"
# password = "zaov rfhj zsjj lbva"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="urigakuru@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of the email")
#


import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)