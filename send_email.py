import smtplib
from email.mime.text import MIMEText
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

sender = os.getenv("SENDER_EMAIL")
# App password for Gmail for tylertam571news@gmail.com
app_password = os.getenv("APP_PASSWORD")
recipient = os.getenv("RECIPIENT_EMAIL")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Write an email to my friend " + recipient + ", about how this email was sent using the Gemini API in Python. Make it fun and lighthearted."
)

msg = MIMEText(response.text)
msg["Subject"] = "from tyler using Gemini API"
msg["From"] = sender
msg["To"] = recipient

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, app_password)
    server.send_message(msg)

print("Email sent!")
