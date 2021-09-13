#!/usr/bin/python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys

msg = MIMEMultipart()

# Your SMTP server
server = smtplib.SMTP(host='mail.example.com',port=25)
# E-mail From
msg['From'] = "admin@axample.com"

# When 4 args
if len(sys.argv) == 4:
        msg['To'] = sys.argv[3] + "@example.com"
        msg['Subject'] = "Пропущен звонок от " + sys.argv[1] + " (" + sys.argv[2] + ")"
        message = "Вам звонил абонент " + sys.argv[1] + " (" + sys.argv[2] + ") на номер " + sys.argv[3]

# When 3 args
elif len(sys.argv) == 3:
        msg['To'] = sys.argv[2] + "@capital.local"
        msg['Subject'] = "Пропущен звонок от " + sys.argv[1]
        message = "Вам звонил абонент " + sys.argv[1] + " на номер " + sys.argv[2]

else:
        print("Wrong args!")

# Send message
msg.attach(MIMEText(message, 'plain'))
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
