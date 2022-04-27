#This will contain unit tests for the Menace
from asyncio.windows_events import NULL
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import game_board
from main import menace

class MenaceTest(unittest.TestCase):
    def test_move_to_make(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', ' ',]
        game_board_test.set_game_board(test_board)
        
        menace_obj = menace.Menace()
        received_game_board = game_board_test.get_game_board()
        self.assertEqual(menace_obj.move_to_make(game_board_test), 8)