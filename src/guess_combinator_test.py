import unittest

from filter import Filter
from differ import Differ
from guess_combinator import GuessCombinator


class TestGuessCombinator(unittest.TestCase):
  def test_it_exists(self):
    self.assertNotEqual(GuessCombinator(), None)

  def test_it_returns_a_best_guess(self):
    # solution_unknown
    corpus = ["abcde", "abcdf", "abcdg", "abcdh", "abcdi", "efghi"]
    expected_best_guess_pair = ["abcde", "efghi"]
    # I can't construct good examples.

    self.assertNotEqual(GuessCombinator.process(
        corpus, corpus), None)


if __name__ == '__main__':
  unittest.main()
