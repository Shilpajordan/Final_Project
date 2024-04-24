from difflib import get_close_matches
import json


def load_knwoledge_base(file_path: str) -> dict:
    # to read the json file
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knwoledge_base(file_path: str, data: dict):
    # to save new answers to our json file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    # to find a close match in our json file
    match: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return match[0] if match else None
    # n=1 give us only 1 answer back and cutoff is giving us back similar answer

def get_answer_for_question(question: str, json_answer: dict) -> str | None:
    # give us the answer back
    for q in json_answer["questions"]:
        if q["question"] == question:
            return q["answer"]
        



def chat_bot():
    #loading the knowledge base
    knowledge_base: dict = load_knwoledge_base("json_answer.json")

    while True:
        user_input: str = input("You ")

        if user_input.lower()=="quit":
            break
        #finding best match with the question
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
        #if noting is found, try to teach
            print("Bot: i don´t know the answer. Can you teach me?")
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knwoledge_base("json_answer.json", knowledge_base)
                print(f"Bot: THX! I got it now")


if __name__ == "__main__":
    chat_bot()