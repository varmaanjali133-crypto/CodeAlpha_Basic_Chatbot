import datetime

def show_help():
    print("\n💡 You can try these commands:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- time")
    print("- date")
    print("- tell me a joke")
    print("- I am happy")
    print("- I am sad")
    print("- calculate")
    print("- help")
    print("- bye\n")


def chatbot():
    print("🤖 Welcome to SmartBot!")
    user_name = input("Before we start, what's your name? ").strip()

    print(f"\nHello {user_name}! Nice to meet you 😊")
    print("Type 'help' to see what I can do.\n")

    while True:
        user = input(f"{user_name}: ").lower().strip()

        if user in ["hello", "hi", "hey"]:
            print("🤖 SmartBot: Hello! Hope you're having a great day.")

        elif user == "how are you":
            print("🤖 SmartBot: I'm doing great. Thanks for asking!")

        elif user == "what is your name":
            print("🤖 SmartBot: My name is SmartBot.")

        elif user == "time":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 SmartBot: Current time is {current_time}")

        elif user == "date":
            today = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 SmartBot: Today's date is {today}")

        elif user == "tell me a joke":
            print("🤖 SmartBot: Why do programmers prefer dark mode? Because light attracts bugs 😄")

        elif user == "hehe":
            print("🤖 SmartBot: Haha😄,You liked it 😊")

        elif "happy" in user:
            print("🤖 SmartBot: That's wonderful! Keep smiling 😊")

        elif "sad" in user:
            print("🤖 SmartBot: I'm sorry to hear that. Things will get better ❤️")

        elif user == "calculate":
            try:
                expression = input("Enter calculation (example: 5+3): ")
                result = eval(expression)
                print(f"🤖 SmartBot: Answer = {result}")
            except:
                print("🤖 SmartBot: Invalid calculation.")

        elif user == "help":
            show_help()

        elif user == "bye":
            print(f"🤖 SmartBot: Goodbye, {user_name}! Have a great day 🌸")
            break

        else:
            print("🤖 SmartBot: Sorry, I didn't understand that. Type 'help'.")


# Run chatbot
chatbot()