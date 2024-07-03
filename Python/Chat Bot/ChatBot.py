import nltk
from nltk.chat.util import Chat, reflections

# Ensure the required NLTK data packages are downloaded
nltk.download('punkt')

# Define a set of pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Python. You can call me PyBot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am fine",
        ["Great to hear that", "How can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon.", "It was nice talking to you. Goodbye."]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the chatbot
def chatbot_start():
    print("Hi, I'm PyBot. How can I assist you today?")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot_start()   