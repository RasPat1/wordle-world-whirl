from .wordle import Wordle
import unittest

class TestWordleMethods(unittest.TestCase):

  def test_it_runs(self):
    self.assertEqual(Wordle.main(), None)


if __name__ == '__main__':
    unittest.main()
