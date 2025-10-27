from google import genai

class GeminiWrapper:
    def __init__(self, api_key, model="gemini-2.5-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.conversation_history = []

    def send_message(self, message):
        # Add user message to the conversation history
        self.conversation_history.append({"role": "user", "content": message})
        
        # Generate content using the Gemini API
        response = self.client.models.generate_content(
            model=self.model,
            contents=self._format_conversation()
        )
        
        # Add AI response to the conversation history
        self.conversation_history.append({"role": "ai", "content": response.text})
        
        return response.text

    def _format_conversation(self):
        # Format the conversation history for the API
        return "\n".join([f"{entry['role']}: {entry['content']}" for entry in self.conversation_history])

    def clear_history(self):
        # Clear the conversation history
        self.conversation_history = []

# Example usage
if __name__ == "__main__":
    API_KEY = "AIzaSyDl21kgUVZvzWM-bgOuymFEEnNIhqzS-jo"
    gemini = GeminiWrapper(api_key=API_KEY)

    print("Start chatting with Gemini! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = gemini.send_message(user_input)
        print(f"Gemini: {response}")