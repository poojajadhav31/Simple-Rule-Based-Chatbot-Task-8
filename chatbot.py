def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Help section
    elif "help" in user_input:
        return "Sure! You can ask me about Python, tasks, or general queries."

    # Asking about Python
    elif "python" in user_input:
        return "Python is a powerful, beginner-friendly programming language."

    # Asking about internships
    elif "internship" in user_input:
        return "Internships help you gain real-world experience."

    # Asking about task details
    elif "task" in user_input:
        return "Each task builds your Python skills. Which task are you working on?"

    # Exit command
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day."

    # Default fallback
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Take care.")
            break
        
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)

if __name__ == "__main__":
    main()
