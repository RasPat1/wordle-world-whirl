from .game_runner import GameRunner

import unittest


class TestGameRunnerMethods(unittest.TestCase):

  def testCreatesAGame(self):
    self.assertNotEqual(GameRunner(), None)
