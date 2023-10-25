from io import StringIO
import unittest
from unittest.mock import patch
from app import *



class TestGame(unittest.TestCase):


    def test_random_num_generator(self):
        code = random_num_generator()
        self.assertTrue(code >= 1)
        self.assertTrue(code <= 6)

    @patch('builtins.input', side_effect=['owami'])
    def test_user_name(self,_):
        name = user_name()
        self.assertTrue(len(name) > 3)
        self.assertTrue(len(name) < 10)
        self.assertTrue(name.isalpha())

    @patch('builtins.input', side_effect=['owami'])
    def test_play_game(self, _):
        name = user_name()
        
        expectedOutput = f"""{name} : 1
        Computer : 2
        Computer is the Winner!"""
        with patch('sys.stdout', new = StringIO()) as output:
            play_game(name, 2, 1)
            play_game(name, 4, 6)
            play_game(name, 3, 4)
            self.assertEqual(output.getvalue(), expectedOutput) 
