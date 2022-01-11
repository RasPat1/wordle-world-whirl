import unittest

from minimal_path import MinimalPath
# from minimal_path import Differ
from minimal_path import Filter
from reader import Reader

import cProfile

_SMALL_UNITTEST_SOLUTIONS_PATH = "data/unittest_data/small_solution_set"
_SMALL_UNITTEST_GUESS_PATH = "data/unittest_data/small_guess_set"

_SMALL_SET = "data/small_test_set_1"
_MEDIUM_SET = "data/medium_test_set_1"


class TestMinimalPathMethods(unittest.TestCase):

  def test_it_runs(self):
    corpus = ['aa', 'bb', 'cc', 'ab']
    expected_best_guess = 'ab'
    result = MinimalPath.best_guess(corpus)
    print(result)
    (best_guess, path, avg_length) = result
    self.assertEqual(best_guess, expected_best_guess)

  def test_it_runs_on_real_example(self):
    corpus = ['rogue', 'horde', 'ombre', 'rouge', 'forge', 'gorge']
    expected_best_guesses = ['forge', 'gorge']  # forge or gorge right?
    result = MinimalPath.best_guess(corpus)
    print(result)
    (best_guess, path, avg_length) = result
    self.assertIn(best_guess, expected_best_guesses)

  def test_it_on_bigger_corpus(self):
    (corpus, _) = Reader.load_lists(
        _SMALL_UNITTEST_SOLUTIONS_PATH, _SMALL_UNITTEST_GUESS_PATH)
    result = MinimalPath.best_guess(corpus)
    print(result)
    (best_guess, path, avg_length) = result
    self.assertEqual(avg_length, 1.375)

  def test_it_on_medium_corpus(self):
    (corpus, _) = Reader.load_lists(
        _MEDIUM_SET, _MEDIUM_SET)
    result = MinimalPath.best_guess(corpus)
    print(result)
    (best_guess, path, avg_length) = result
    self.assertEqual(best_guess, 'react')

# We're juse using the old differ for now.
# class TestDifferMethods(unittest.TestCase):

#   def test_it_diffs_two_words(self):
#     guess = "choke"
#     solution = "chess"
#     expected_diff_result = ({'o', 'k'}, {'c': [0], 'h': [1]}, {'e': [4]})
#     diff_result = Differ.diff(guess, solution)
#     self.assertEqual(diff_result, expected_diff_result)

#   def test_handles_multiple_instances_of_same_char_in_word_correctly(self):
#     cases = [
#         ("stash", "chase", ({'s', 't'}, {'a': [2], 's': [3]}, {'h': [4]})),
#         # ("swear", "busts", [_CLOSE, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
#         # ("aaabb", "cccca", [_CLOSE, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
#         # ("aaabb", "acccc", [_MATCH, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
#         # ("aaabb", "acacc", [_MATCH, _ABSENT, _MATCH, _ABSENT, _ABSENT]),
#         # ("aaabb", "acaca", [_MATCH, _CLOSE, _MATCH, _ABSENT, _ABSENT]),
#         # ("bbaaa", "acaca", [_ABSENT, _ABSENT, _MATCH, _CLOSE, _MATCH]),
#         # ("bbaaa", "ccaca", [_ABSENT, _ABSENT, _MATCH, _ABSENT, _MATCH]),
#     ]
#     for case in cases:
#       guess = case[0]
#       solution = case[1]
#       expected_diff_result = case[2]
#       with self.subTest(name=(guess, solution)):
#         diff_result = Differ.diff(guess, solution)
#         self.assertEqual(diff_result, expected_diff_result)


if __name__ == '__main__':
  # cProfile.run('unittest.main()')
  unittest.main()
