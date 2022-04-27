#This will contain unit tests for the human
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import human
from main import game_board

class HumanTest(unittest.TestCase):

    def test_block_two_in_a_row(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.block_two_in_a_row(test_board), 2)

    def test_two_in_a_row(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = ['O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.two_in_a_row(test_board), 2)
    
    def test_center(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.center(test_board), 4)

    def test_opposite_corner(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.opposite_corner(test_board), 8)

    def test_empty_corner(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.empty_corner(test_board), 8)

    def test_empty_side(self):
        game_board_test = game_board.Game_Board()
        human_test = human.Human()
        test_board = [' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertEqual(human_test.empty_side(test_board), 7)