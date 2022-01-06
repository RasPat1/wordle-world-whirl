from .wordle import Wordle
import unittest


class TestWordleMethods(unittest.TestCase):

  def test_it_runs(self):
    solution_test_path = Wordle._SOLUTION_GUESS_PATH
    guess_test_path = Wordle._TEST_GUESS_PATH
    self.assertEqual(Wordle.process(solution_test_path, guess_test_path), None)


if __name__ == '__main__':
  unittest.main()
