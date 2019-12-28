#!/usr/bin/python

import smtplib

sender = 'skuzzymiglet@gmail.com'
receivers = ['skuzzymiglet@gmail.com']

message = """From: From Person <skuzzymiglet@gmail.com>
To: To Person <skuzzymiglet@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('mail.gmail.com', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
