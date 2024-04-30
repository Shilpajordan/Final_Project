import unittest
from unittest.mock import patch
import json
from io import StringIO
from bot3 import load_knowledge_base, find_best_match, get_answer_for_question, chat_bot

class TestBot3(unittest.TestCase):

    def test_load_knowledge_base(self):
        test_data = {
            "Intents": [
                {"tag": "Greeting", "patterns": ["Hi", "Hello"], "responses": ["Hi there!", "Hello!"]}
            ]
        }
        with open("test_intents.json", "w") as test_file:
            json.dump(test_data, test_file)
        self.assertEqual(load_knowledge_base("test_intents.json"), test_data)
    
    def test_get_answer_for_question(self):
        test_data = {
            "Intents": [
                {"tag": "Greeting", "patterns": ["Hi", "Hello"], "responses": ["Hi there!", "Hello!"]}
            ]
        }
        self.assertIn(get_answer_for_question("Hi", test_data), ["Hi there!", "Hello!"])
        self.assertEqual(get_answer_for_question("Goodbye", test_data), "I don't know")

    @patch('builtins.input', side_effect=["hi", "quiet"])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('bot3.get_answer_for_question', return_value="Hi there!")
    def test_chat_bot(self, mock_get_answer, mock_stdout, mock_input):
        chat_bot()
        self.assertEqual(mock_stdout.getvalue(), "Bot: Hi there!\n")

    def test_find_best_match(self):
        test_intents = {
            "Greeting": ["hi", "hello", "hey"],
            "Farewell": ["bye", "goodbye", "see you later"]
        }
        self.assertEqual(find_best_match("hi", test_intents), "Greeting")
        self.assertEqual(find_best_match("bye", test_intents), "Farewell")

if __name__ == "__main__":
    unittest.main()