from scorer import Scorer
from differ import Differ

import unittest


class TestScorerMethods(unittest.TestCase):

  def test_it_scores(self):
    guess = "choke"
    # solution = "chess"
    diff = [Differ.MATCH, Differ.MATCH,
            Differ.ABSENT, Differ.ABSENT, Differ.CLOSE]
    dictionary = ["choke", "chode", "chose", "chess", "clops", "ocean"]
    expected_score = 5
    score = Scorer.get_corpus_reduction_score(
        guess, diff, dictionary, {}, {})
    self.assertEqual(score, expected_score)

  def test_it_includes_itself(self):
    guess = "aaaaa"
    # solution = "aaaaa"
    diff = [Differ.MATCH, Differ.MATCH,
            Differ.MATCH, Differ.MATCH, Differ.MATCH]
    dictionary = ["aaaaa"]
    expected_score = 0
    score = Scorer.get_corpus_reduction_score(
        guess, diff, dictionary, {}, {})
    self.assertEqual(score, expected_score)

  def test_it_includes_itself_with_bigger_dict(self):
    guess = "aaaaa"
    # solution = "baaaa"
    diff = [Differ.ABSENT, Differ.MATCH,
            Differ.MATCH, Differ.MATCH, Differ.MATCH]
    dictionary = ["aaaaa", "baaaa", "caaaa", "daaaa", "eaaaa"]
    expected_score = 1
    score = Scorer.get_corpus_reduction_score(
        guess, diff, dictionary, {}, {})
    self.assertEqual(score, expected_score)


if __name__ == '__main__':
  unittest.main()
