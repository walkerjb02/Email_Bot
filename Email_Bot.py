import smtplib, ssl
import pandas as pd

data = pd.read_csv('AIG.csv') #<--- Put in the CSV you want to iterate through
port = 465
smtp_server = "smtp.gmail.com"
sender_email = #Input your email
password = #Input your email password
message = f"""\
Subject: #Put Subject here

Hi!

# Put your message here
"""
context = ssl.create_default_context()

for i in data['Email']: # <--- Put name of column you want to iterate through here
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, i, message.encode())
    except TypeError:
        pass
