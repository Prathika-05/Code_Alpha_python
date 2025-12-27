def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi! Nice to meet you 😊"

    elif user_input in ["how are you", "how are you?", "how r u"]:
        return "I'm fine, thanks! How can I help you?"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot."

    elif user_input in ["help", "support"]:
        return "Sure! You can say hello, ask how I am, or say bye."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day 👋"

    else:
        return "Sorry, I don't understand that. Please try something else."


print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    response = chatbot_response(user_message)
    print("Chatbot:", response)

    if user_message.lower() in ["bye", "goodbye", "exit"]:
        break
