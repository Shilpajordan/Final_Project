from difflib import get_close_matches
import json
import random

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data

def find_best_match(user_question: str, intents: list[str]) -> str | None:
    matches = [(get_close_matches(user_question, pattern, n=1, cutoff=0.6), tag) for tag, pattern in intents.items()]
    best_match = max(matches, key=lambda x: x[0], default=(None, None))
    return best_match[1] if best_match[0] else None

def get_answer_for_question(question: str, json_answer: dict) -> str | None:
    default_response = "I don't know"
    for intent in json_answer["Intents"]:
        if question in intent["patterns"]:
            return random.choice(intent["responses"])
    
    return default_response
            

def chat_bot():
    knowledge_base: dict = load_knowledge_base("intents.json")
    intents = {intent['tag']: intent['patterns'] for intent in knowledge_base['Intents']}

    while True:
        user_input: str = input("You: ")

        if user_input == "quiet":
            break

        best_match: str | None = find_best_match(user_input, intents)

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print(f"Bot: I don't know.")

if __name__ == "__main__":
    chat_bot()
