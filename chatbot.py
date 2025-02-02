import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you today?", "Hi there! How can I help?"]],
    [r"what is your name\??", ["I am a chatbot created to assist you!", "My name is Chatbot, your virtual assistant!"]],
    [r"how are you\??", ["I'm just a program, but I'm functioning as expected. How about you?"]],
    [r"(.*) your purpose\??", ["I am here to assist you with your questions.", "My purpose is to provide information and support."]],
    [r"(.*) created you\??", ["I was created by a Python enthusiast as part of a programming task!"]],
    [r"bye|exit", ["Goodbye! Have a great day!", "See you later! Take care!"]],
    [r"(.*)", ["I'm sorry, I didn't understand that. Could you rephrase?", "Can you elaborate on that?"]],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        # Download NLTK data (only needed the first time)
        nltk.download("punkt", quiet=True)
        start_chatbot()
    except Exception as e:
        print(f"An error occurred: {e}")
