import re
import random

# Define the chatbot's responses
responses = {
    r"hi|hello|hey": ["Hello!", "Hi there!", "Hey!"],
    r"how are you?": ["I'm doing well, thanks for asking!", "Doing good, how about you?"],
    r"what is your name\??": ["My name is Chatbot, nice to meet you!"],
    r"thank you": ["You're welcome!", "No problem!"],
    r"goodbye|bye": ["Goodbye!", "Take care!", "See you later!"],
    r"default": ["I'm afraid I don't understand. Could you please rephrase your question?"]
}

def respond(user_input):
    """
    Respond to the user's input based on the defined responses.
    """
    for pattern, responses_list in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses_list)
    return responses["default"][0]

def main():
    print("Welcome to the Customer Interaction Chatbot!")
    print("You can start chatting with me. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        response = respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()


___________________________________________________________________________________

def get_user_input():
    return input("You: ")

def respond_to_greeting():
    return "Hello! Welcome to our online store. How can I assist you today?"

def ask_for_category():
    return "Sure! What category of products are you interested in? We have electronics, clothing, books, and more."

def ask_for_product():
    return "Great! Which product would you like to know more about?"

def ask_to_confirm_purchase():
    return "Would you like to purchase this item?"

def ask_for_size():
    return "What size do you need? (e.g., small, medium, large)"

def ask_for_color():
    return "What color would you like?"

def provide_recommendation():
    return "Based on your interests, I recommend checking out our latest arrivals in that category."

def thank_you():
    return "Thank you for shopping with us! Is there anything else I can assist you with?"

def apologize():
    return "I'm sorry, I didn't quite get that. Could you please rephrase?"

def main():
    print(respond_to_greeting())

    context = None

    while True:
        user_input = get_user_input().lower()

        if context == "category":
            if user_input in ["electronics", "clothing", "books"]:
                print(ask_for_product())
                context = "product"
            else:
                print("Sorry, we don't have products in that category.")
                context = None
        elif context == "product":
            print(ask_to_confirm_purchase())
            context = "confirm_purchase"
        elif "hi" in user_input or "hello" in user_input:
            print(respond_to_greeting())
        elif "category" in user_input:
            print(ask_for_category())
            context = "category"
        elif "product" in user_input:
            print(ask_for_product())
            context = "product"
        elif "yes" in user_input and context == "confirm_purchase":
            print(thank_you())
            break
        elif "no" in user_input and context == "confirm_purchase":
            print("Okay, no problem. Is there anything else I can assist you with?")
            context = None
        elif "recommendation" in user_input:
            print(provide_recommendation())
        elif "thank you" in user_input or "thanks" in user_input:
            print(thank_you())
            break
        else:
            print(apologize())

if __name__ == "__main__":
    main()


