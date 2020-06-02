import smtplib , ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = input('Sender Adress:\n')
receiver_email = input("Receiver Adress:\n")

#TODO : add input module later 
password =input('PASSWORD:\n')

#ANCHOR : MESSAGE BODY 

message ="""
Subject: Python Test Message 

This message is created in Python VSCode Script.
This is a test message.

"""

#ANCHOR : SSL MODULE
context = ssl.create_default_context()


with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
    server.ehlo()
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
