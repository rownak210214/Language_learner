import unittest
from tkinter import messagebox
from unittest.mock import patch
from bangla_vocabulary import LanguageLearningAppBangla

class TestBanglaTranslationAccuracy(unittest.TestCase):
    def setUp(self):
        self.app = LanguageLearningAppBangla()
        self.app.withdraw()

    def test_translation_accuracy(self):

        test_cases = {
            "apple": "আপেল",
            "banana": "কলা",
            "orange": "কমলা",
            "grape": "আঙ্গুর"
        }
        for english_word, bangla_translation in test_cases.items():
            self.assertEqual(self.app.vocabulary[english_word], bangla_translation)

    def tearDown(self):
        self.app.destroy()

class TestNextWordFunctionality(unittest.TestCase):
    def setUp(self):
        self.app = LanguageLearningAppBangla()

    def test_next_word_functionality(self):

        initial_word = self.app.current_word
        self.app.next_word()
        new_word = self.app.current_word
        self.assertNotEqual(initial_word, new_word)

    def tearDown(self):
        self.app.destroy()


class TestIncorrectTranslationMessage(unittest.TestCase):
    def setUp(self):
        self.app = LanguageLearningAppBangla()

    @patch.object(messagebox, 'showerror')
    def test_incorrect_translation_message(self, mock_showerror):
        # Simulate entering incorrect translation and checking
        self.app.entry_translation.insert(0, "incorrect_translation")
        self.app.check_translation()
        # Assert that the error message box is shown
        mock_showerror.assert_called_once_with("Incorrect", "Your translation is incorrect. Try again.")

    def tearDown(self):
        self.app.destroy()


class TestInitialWordDisplay(unittest.TestCase):
    def setUp(self):
        self.app = LanguageLearningAppBangla()

    def test_initial_word_display(self):
        # Check if the initial word displayed is not empty
        initial_word = self.app.label_word.cget("text")
        self.assertNotEqual(initial_word, "")

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
