#This will contain unit tests for the human
import pytest
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import human
from main import game_board

class HumanTest(unittest.TestCase):

    def test_block_two_in_a_row(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.block_two_in_a_row(test_board), 2)

    def test_block_two_in_a_row(self):
        game_board_test = game_board.Game_Board()
        test_board = ['O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.block_two_in_a_row(test_board), 2)
    
    def test_center(self):
        game_board_test = game_board.Game_Board()
        test_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.center(test_board), 4)

    def test_opposite_corner(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.opposite_corner(test_board), 8)

    def test_empty_corner(self):
        game_board_test = game_board.Game_Board()
        test_board = ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.empty_corner(test_board), 8)

    def test_empty_side(self):
        game_board_test = game_board.Game_Board()
        test_board = [' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ', ' ',]
        test_board = game_board_test.convert_board_to_string()
        self.assertEquals(human.empty_corner(test_board), 7)