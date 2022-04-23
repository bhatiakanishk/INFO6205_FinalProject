#This will contain unit tests for the Menace
from asyncio.windows_events import NULL
import pytest
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
        self.assertEquals(menace_obj.move_to_make(game_board_test), 8)

    # def test_win_result(self):
    #     game_board_test = game_board.Game_Board()
    #     menace_obj = menace.Menace()

    #     moves_played = menace_obj.get_moves_played()
    #     game_states = menace_obj.get_game_states()

    #     test_board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    #     moves_played.append((test_board, 1))
    #     game_states[test_board] = []
    #     for i in range(3):
    #         game_states[game_board].append(1)
        

