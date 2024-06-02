import smtplib, ssl
import os

def sendemail(message):
    host = "smtp.gmail.com"
    port = 465


    username = "okitsmeagain123@gmail.com"
    password = os.getenv("PASSWORD")

    reciever = "okitsmeagain123@gmail.com"
    context = ssl.create_default_context()

 
    with smtplib.SMTP_SSL(host, port,context =context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

