import unittest

from filter import Filter
from differ import Differ


class TestFilterMethods(unittest.TestCase):
  def test_it_exists(self):
    self.assertNotEqual(Filter(), None)

  def test_it_returns_a_best_guess(self):
    guess = "choke"
    # solution = "chess"
    guess_diff = [Differ.MATCH, Differ.MATCH,
                  Differ.ABSENT, Differ.ABSENT, Differ.CLOSE]
    corpus = ["choke", "chode", "chose", "chess", "clops", "ocean"]

    self.assertEqual(Filter().get_best_next_guess(
        guess, guess_diff, corpus, corpus), "chess")


if __name__ == '__main__':
  unittest.main()
