#This will contain unit tests for main
import pytest
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main.main import load_game_states

class MainTest(unittest.TestCase):

    def test_load_game_states(self):
        game_states = load_game_states()
        self.assertGreater(game_states, 0)