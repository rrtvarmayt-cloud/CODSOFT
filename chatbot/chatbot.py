print("===================================")
print("      CODSOFT AI CHATBOT")
print("===================================")
print("Hello! I am your AI chatbot.")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ")

    user = user.lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: My name is CodSoft Bot.")

    elif user == "who created you":
        print("Bot: Yuvan created me.")

    elif user == "what can you do":
        print("Bot: I can chat with you.")

    elif user == "tell me a joke":
        print("Bot: Why don't scientists trust atoms? Because they make up everything!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break
        
    else:
        print("Bot: I don't understand.") 
