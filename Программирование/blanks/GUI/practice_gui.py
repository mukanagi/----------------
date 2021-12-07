import smtplib
from tkinter import Message

sender = "fedorhuyakin@gmail.com"
receiver = "nemoseth@yandex.ru"
password = 'BSD7y89032dSHOIDg1#@#AS!'
subject = "Тест"
body = "Это я такую прогу написал, которая отправялет письма!"

message = f"""From:{sender}
To:{receiver}
Subject:{subject}\n
Body:{body}
"""
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.starttls()

server.login(sender, password)
print('Logged in...')

server.sendmail(sender, receiver, message)
print("Email has been sent!")