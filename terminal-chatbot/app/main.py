import atexit

from app.services.chatbot_service import ChatbotService
from dotenv import load_dotenv

load_dotenv()

chatbot_service = ChatbotService()


def close_chatbot_connections():
    chatbot_service.close_client()


atexit.register(close_chatbot_connections)


def main():
    try:
        print("\nWelcome to terminal chatbot!\n")
        user_name: str = input("Enter your name to start: ")
        
        stateful_response: str = input("Do you want to use stateful chatbot? (y/n): ").lower().strip()
        stateful: bool = stateful_response == 'y' or stateful_response == 'yes'
        
        structured_output_response: str = input("Do you want to use JSON structured output? (y/n): ")
        structured_output: bool = structured_output_response == 'y' or structured_output_response == 'yes'
        
        print("--------------------------------")
        print(f"Hello {user_name}, start chatting with the terminal chatbot.")
        print("--------------------------------")

        while True:
            user_message = input(f"{user_name}: ")

            if not user_message.strip():
                continue

            response = chatbot_service.send_message(user_message, stateful, structured_output)

            print(f"Bot: {response.content}")
    except KeyboardInterrupt:
        print("\n\n[System] Chat session ended.")


if __name__ == '__main__':
    main()
