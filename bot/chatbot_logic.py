import json
import random
from difflib import get_close_matches
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv


# Loading the env
load_dotenv()

waiting_for_feedback = False


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)
    return data

def find_best_match(user_question: str, intents: list[str]) -> str | None:
    matches = [(get_close_matches(user_question, pattern, n=1, cutoff=0.8), tag) for tag, pattern in intents.items()]
    best_match = max(matches, key=lambda x: x[0], default=(None, None))
    return best_match[1] if best_match[0] else None

def get_answer_for_question(question: str, json_answer: dict) -> str | None:
    for intent in json_answer["Intents"]:
        if question in intent["patterns"]:
            return random.choice(intent["responses"])

def get_all_doctors():
    try:
        
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cursor = conn.cursor()
        
        query = "SELECT first_name, last_name, specialization FROM doc_search_doctor"
        cursor.execute(query)
        doctors = cursor.fetchall()
        
      
        cursor.close()
        conn.close()
        
        return doctors
    except psycopg2.Error as error:
        print("Error querying PostgreSQL database:", error)
        return None

def collect_feedback(feedback):
    with open("feedback.txt", "a") as file:
        file.write(feedback + "\n")
    global waiting_for_feedback
    waiting_for_feedback = False
    return "Thank you for your feedback!"

def chat_bot(user_input):
    global waiting_for_feedback

    
    user_input = user_input.strip().lower()  
    print(f"User input: {user_input}")

    if waiting_for_feedback:
        return collect_feedback(user_input)  # If waiting for feedback, treat the input as feedback
    elif user_input == "give feedback":
        waiting_for_feedback = True
        return "Please write your feedback:"
    
    else:
        knowledge_base: dict = load_knowledge_base("intents.json")
        intents = {intent['tag']: intent['patterns'] for intent in knowledge_base['Intents']}
        best_match = find_best_match(user_input, intents)
        if best_match:
            return get_answer_for_question(best_match, knowledge_base)
        elif user_input.lower() == "show doctors":
            all_doctors = get_all_doctors()
            if all_doctors:
                return "Here are all the doctors: " + ", ".join(f"{doctor[0]} {doctor[1]} {doctor[2]}" for doctor in all_doctors)
            else:
                return "There are no doctors in the database."
        else:
            return "I don't know. If you want information about our doctors, write 'show doctors'. If you want to give us feedback, write 'give feedback'."

