import json
import random


def load_intents(file_path: str) -> dict:
    # Load intents from the JSON file
    with open(file_path, 'r',encoding='utf-8' ) as file:
        intents_data = json.load(file)
    return intents_data

def get_intent(user_input: str, intents_data: dict) -> dict:
    # Identify the matching intent based on user input
    best_match = None
    best_score = 0

    for intent in intents_data['Intents']:
        for pattern in intent['patterns']:
            # Calculate similarity score based on the length of the longest common substring
            similarity_score = len(set(user_input.lower()) & set(pattern.lower()))
            if similarity_score > best_score:
                best_match = intent
                best_score = similarity_score

    return best_match

def get_random_response(intent: dict) -> str:
    # Select a random response from the possible responses of the identified intent
    responses = intent['responses']
    return random.choice(responses) if responses else None

def chat_bot():
    # Load intents from the JSON file
    intents_data = load_intents("intents.json")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "quit":
            break

        # Identify the matching intent for the user input
        matched_intent = get_intent(user_input, intents_data)

        if matched_intent:
            # Select a random response from the possible responses of the matched intent
            response = get_random_response(matched_intent)
            if response:
                print(f"Bot: {response}")
        else:
            print("Bot: Sorry, I don't understand.")

if __name__ == "__main__":
    chat_bot()
