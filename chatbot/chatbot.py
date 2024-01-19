import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you.', 'I am fine, how about you?']),
    (r'what is your name', ['I am a simple chatbot.', 'You can call me ChatGPT.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye! Take care.']),
    # Add more patterns and responses as needed
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

def run_chat():
    print("Chatbot: Hi! I'm your chatbot. Ask me anything or say goodbye to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break

        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    run_chat()
