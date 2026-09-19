from agent import Agent


def main():

    agent = Agent()

    print("Scalable Agentic System")
    print("Type 'exit' to stop.")

    while True:

        message = input("\nUser: ")

        if message.lower() == "exit":
            print("Goodbye!")
            break

        result = agent.chat(message)

        print("\nSelected Tool:",
              result["selected_tool"])

        print("Agent:",
              result["message"])

        print("Result:",
              result["result"])


if __name__ == "__main__":
    main()
