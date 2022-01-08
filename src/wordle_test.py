from wordle import Wordle
import wordle
import unittest

_SMALL_UNITTEST_SOLUTIONS_PATH = "../data/unittest_data/small_solution_set"
_SMALL_UNITTEST_GUESS_PATH = "../data/unittest_data/small_guess_set"


class TestWordleMethods(unittest.TestCase):

  def test_it_runs(self):
    w = Wordle(_SMALL_UNITTEST_SOLUTIONS_PATH,
               _SMALL_UNITTEST_GUESS_PATH)
    self.assertEqual(w.process(), None)


if __name__ == '__main__':
  unittest.main()
