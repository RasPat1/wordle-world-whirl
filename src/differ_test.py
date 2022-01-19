from differ import Differ

import unittest

_MATCH = Differ.MATCH
_ABSENT = Differ.ABSENT
_CLOSE = Differ.CLOSE


class TestDifferMethods(unittest.TestCase):

  def test_it_diffs_two_words(self):
    guess = "choke"
    solution = "chess"
    expected_diff_result = [_MATCH, _MATCH, _ABSENT, _ABSENT, _CLOSE]
    diff_result = Differ.diff(guess, solution, {})
    self.assertEqual(diff_result, expected_diff_result)

  # What happens when a letter appears twice in the guess and once in the solution?
  # One yellow right?
  def test_handles_multiple_instances_of_same_char_in_word_correctly(self):
    # The word is query
    # "roars", "query" -> result is blank ,blank blank match blank
    cases = [
        ("stash", "chase", [_ABSENT, _ABSENT, _MATCH, _MATCH, _CLOSE]),
        ("swear", "busts", [_CLOSE, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
        ("aaabb", "cccca", [_CLOSE, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
        ("aaabb", "acccc", [_MATCH, _ABSENT, _ABSENT, _ABSENT, _ABSENT]),
        ("aaabb", "acacc", [_MATCH, _ABSENT, _MATCH, _ABSENT, _ABSENT]),
        ("aaabb", "acaca", [_MATCH, _CLOSE, _MATCH, _ABSENT, _ABSENT]),
        ("bbaaa", "acaca", [_ABSENT, _ABSENT, _MATCH, _CLOSE, _MATCH]),
        ("bbaaa", "ccaca", [_ABSENT, _ABSENT, _MATCH, _ABSENT, _MATCH]),
    ]
    for case in cases:
      guess = case[0]
      solution = case[1]
      expected_diff_result = case[2]
      with self.subTest(name=(guess, solution)):
        diff_result = Differ.diff(guess, solution, {})
        self.assertEqual(diff_result, expected_diff_result)

  def test_throws_error_on_malformed_input(self):
    pass


if __name__ == '__main__':
  unittest.main()
