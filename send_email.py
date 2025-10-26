import smtplib
from email.mime.text import MIMEText

sender = "tylertam571@gmail.com"
# App password for Gmail for tylertam571news@gmail.com
app_password = "osya bxoi hbgr zadh"
recipient = "liumax2003@gmail.com"

msg = MIMEText("Heyyyyy Body Text heyyyyyyy")
msg["Subject"] = "Subject Hiiiiii"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, app_password)
    for i in range(3):
        server.send_message(msg)

print("Email sent!")
