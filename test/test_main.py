#This will contain unit tests for main

import pytest
import unittest
import sys
import os
sys.path.append(os.getcwd())
from main import main

class MainTest(unittest.TestCase):

    def test_load_game_states(self):
        game_states = main.load_game_states()
        self.assertGreater(game_states, 0)