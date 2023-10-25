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
        
    def test_keep_score(self):
        computer_score,user_score = keep_score(5,1, 1, 0)
        self.assertEqual(computer_score, 0)
        self.assertEqual(user_score, 2)
        computer_score,user_score = keep_score(3,6, 0, 2)
        self.assertEqual(computer_score, 3)
        self.assertEqual(user_score, 0)

    @patch('builtins.input', side_effect=['owami'])
    def test_play_game(self, _):
        name = user_name()
        
        expectedOutput = f"""{name} : 0
Computer : 1
{name} : 0
Computer : 2
{name} : 0
Computer : 3
Computer is the Winner!"""
        with patch('sys.stdout', new = StringIO()) as output:
            with patch('random.randint', side_effect=[4,5, 3,6, 1,2]):
                playgame(name)
                self.assertEqual(output.getvalue(), expectedOutput)
