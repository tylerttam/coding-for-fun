from google import genai

API_KEY = "AIzaSyDl21kgUVZvzWM-bgOuymFEEnNIhqzS-jo"
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Write an email to my friend Josh, about how this email was sent using the Gemini API in Python. Make it fun and lighthearted."
)

print(response.text)