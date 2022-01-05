from .scorer import Scorer

import unittest

class TestScorerMethods(unittest.TestCase):

  # If the result has a match for the first intance of a letter, but another result has a match for the same letter but at the second instance it may have a different match result. We need the location of the "In word, not here" result to be stable. What it really represents is that there is 1 instance of this letter in the solution and our data structure shoudl represent that too. aka get a better data structure for the matches.

  def test_it_scores(self):
    guess = "choke"
    solution = "chess"
    dictionary = ["choke", "chode", "chose", "chess", "clops", "ocean"]
    expected_score = 5
    score = Scorer.get_score(guess, solution, dictionary, {}, {})
    self.assertEqual(score, expected_score)

  def test_it_includes_itself(self):
    guess = "aaaaa"
    solution = "aaaaa"
    dictionary = ["aaaaa"]
    expected_score = 0
    score = Scorer.get_score(guess, solution, dictionary, {}, {})
    self.assertEqual(score, expected_score)

def test_it_includes_itself(self):
    guess = "aaaaa"
    solution = "baaaa"
    dictionary = ["aaaaa", "baaaa", "caaaa", "daaaa", "eaaaa"]
    expected_score = 1
    score = Scorer.get_score(guess, solution, dictionary, {}, {})
    self.assertEqual(score, expected_score)

if __name__ == '__main__':
    unittest.main()
