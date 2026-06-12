from app.services.classifier_service import ClassifierService
from dotenv import load_dotenv

load_dotenv()

classifier_service = ClassifierService()

def main() -> None:
    print("\n**** Welcome to support ticket classifier ****\n")
    print("Please type/paste your issue here. We will classify it in 4 categories:")
    print("1. Billing")
    print("2. Technical support")
    print("3. Account access")
    print("4. General inquiry")
    print("If you want to exit please type exit.")
    print("\n")

    use_json_output = input("Do you want the output in JSON format? (y/n): ")
    if use_json_output == "y":
        use_json_output = True
    else:
        use_json_output = False

    while True:
        user_input = input("\nType/paste your issue description here: ")
        if user_input == "exit":
            break
        
        result, token_usage = classifier_service.classify(user_input, use_json_output)

        if use_json_output:
            print("\nOutput:", result.model_dump_json(indent=4))
            print("\nTokens used:", token_usage.total_token_count)
        else:
            print("\nYour issue is classified as:", result)
            print("\nTokens used:", token_usage.total_token_count)

if __name__ == "__main__":
    main()
