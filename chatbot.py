# faq_chatbot.py
# A simple FAQ chatbot using Python dictionaries

def main():
    # Predefined FAQ database
    faq = {
        "what is your name": "I am a simple FAQ chatbot.",
        "how are you": "I'm just a program, but I'm doing great!",
        "what is python": "Python is a high-level, interpreted programming language known for its readability.",
        "who created you": "I was created by a Python developer as a demo chatbot.",
        "bye": "Goodbye! Have a great day!"
    }

    print("🤖 FAQ Chatbot (type 'bye' to exit)")
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input == "bye":
            print("Bot:", faq["bye"])
            break

        # Respond if question exists
        response = faq.get(user_input, "Sorry, I don't know the answer to that.")
        print("Bot:", response)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBot: Goodbye!")
