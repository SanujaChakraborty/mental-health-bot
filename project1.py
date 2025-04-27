import random

# Predefined simple queries
responses = {
    "hi": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "hello": ["Hello!", "Hi there!", "Hey! Need any help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling operational! How can I assist you?"],
    "what is your name": ["I'm your friendly chatbot!", "You can call me ChatBuddy."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "thank you": ["You're welcome!", "Anytime!", "Glad I could help!"],
}

# Function to get a response
def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    
    # check if user_input matches the known queries
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
        
    # if input not recognize
    return "I'm sorry, I don't understand that. Can you ask something else"

# main chat loop
def chat():
    print("ChatBot: Hello! Ask me anything. (Type 'exit' to end)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = get_bot_response(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()