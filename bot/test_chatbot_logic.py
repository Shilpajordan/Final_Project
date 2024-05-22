import unittest
from unittest.mock import patch, mock_open, MagicMock



from chatbot_logic import (
    load_knowledge_base,
    find_best_match,
    get_answer_for_question,
    get_all_doctors,
    collect_feedback,
    chat_bot
)

class TestChatBot(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='{"Intents": [{"tag": "greeting", "patterns": ["hello"], "responses": ["Hi there!"]}]}')
    def test_load_knowledge_base(self, mock_file):
        data = load_knowledge_base("intents.json")
        self.assertEqual(data, {"Intents": [{"tag": "greeting", "patterns": ["hello"], "responses": ["Hi there!"]}]})

    def test_find_best_match(self):
        intents = {"greeting": ["hello", "hi"], "goodbye": ["bye", "see you"]}
        self.assertEqual(find_best_match("hello", intents), "greeting")
        self.assertEqual(find_best_match("bye", intents), "goodbye")
        self.assertIsNone(find_best_match("unknown", intents))

    
    def test_get_answer_for_question(self):
        json_answer = {
            "Intents": [
                {
                    "tag": "Hallo",
                    "patterns": ["hello"],
                    "responses": ["Hi there!", "Hello!"]
                }
            ]
        }
        self.assertEqual(get_answer_for_question("hello", json_answer), "Hi there!")
        self.assertIsNone(get_answer_for_question("bye", json_answer))

    @patch("sqlite3.connect")
    def test_get_all_doctors(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [("Dr. John Doe",), ("Dr. Jane Doe",)]
        mock_connect.return_value = mock_conn

        doctors = get_all_doctors()
        self.assertEqual(doctors, [("Dr. John Doe",), ("Dr. Jane Doe",)])

        mock_cursor.execute.assert_called_once_with("SELECT * FROM doc_search_doctor")
        mock_conn.close.assert_called_once()

    @patch("builtins.open", new_callable=mock_open)
    def test_collect_feedback(self, mock_file):
        response = collect_feedback("Great service!")
        self.assertEqual(response, "Thank you for your feedback!")
        mock_file().write.assert_called_once_with("Great service!\n")

    @patch("builtins.open", new_callable=mock_open, read_data='{"Intents": [{"tag": "hello", "patterns": ["hello"], "responses": ["Hi there!"]}]}')
    def test_chat_bot(self, mock_file):
        global waiting_for_feedback
        waiting_for_feedback = False
        
        # Test normal interaction
        self.assertEqual(chat_bot("hello"), "Hi there!")
        
        # Test giving feedback
        self.assertEqual(chat_bot("give feedback"), "Please write your feedback:")
        waiting_for_feedback = True
        self.assertEqual(chat_bot("Great service!"), "Thank you for your feedback!")
        
        # Test unknown input
        waiting_for_feedback = False
        self.assertEqual(chat_bot("unknown input"), "I don't know. If you want information about our doctors, write 'show doctors'. If you want to give us feedback, write 'give feedback'.")

    @patch("chatbot_logic.get_all_doctors")
    def test_chat_bot_show_doctors(self, mock_get_all_doctors):
        mock_get_all_doctors.return_value = [("Dr. John Doe",), ("Dr. Jane Doe",)]
        self.assertEqual(chat_bot("show doctors"), "Here are all the doctors: ('Dr. John Doe',), ('Dr. Jane Doe',)")
        
        mock_get_all_doctors.return_value = None
        self.assertEqual(chat_bot("show doctors"), "There are no doctors in the database.")


if __name__ == "__main__":
    unittest.main()