print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hello there!")
    
    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great!")
    
    elif "name" in user_input:
        print("🤖 Chatbot: I'm your assistant chatbot.")
    
    elif "help" in user_input:
        print("🤖 Chatbot: I can respond to greetings and simple questions.")
    
    elif "bye" in user_input:
        print("🤖 Chatbot: Goodbye!")
        break
    
    else:
        print("🤖 Chatbot: I don't understand that yet.")