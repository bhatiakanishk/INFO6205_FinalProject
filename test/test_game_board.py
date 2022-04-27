# This will contain unit tests for the Game Board

import pytest
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import game_board

class GameBoardTest(unittest.TestCase):
    
    def test_win_condition(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ',]
        game_board_test.set_game_board(test_board)
        self.assertTrue(game_board_test.win_condition())

    def test_draw_condition(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', 'X', '0', 'X', 'X', '0', '0', '0', 'X',]
        game_board_test.set_game_board(test_board)
        self.assertTrue(game_board_test.draw_condition())

    def test_make_move_on_board(self):
        game_board_test = game_board.Game_Board()
        game_board_test.make_move_on_board(0, "X")
        received_game_board = game_board_test.get_game_board()
        self.assertEqual(received_game_board[0], "X")

    def test_is_move_valid(self):
        game_board_test = game_board.Game_Board()
        received_game_board = game_board_test.get_game_board()
        self.assertFalse(game_board_test.is_move_valid(10, game_board_test))