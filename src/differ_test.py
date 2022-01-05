from .differ import Differ

import unittest

class TestDifferMethods(unittest.TestCase):

  def test_it_diffs_two_words(self):
    guess = "choke"
    solution = "chess"
    expected_diff_result = [2, 2, 0, 0, 1]
    diff_result = Differ.get_diff_result(guess, solution)
    self.assertEqual(diff_result, expected_diff_result)

  # What happens when a letter appears twice in the guess and once in the solution?
  # One yellow right?
  def test_handles_multiple_instances_of_same_char_in_word_correctly(self):
    cases = [
      ("stash", "chase", [0, 0, 2, 2, 1]),
      ("swear", "busts", [1, 0, 0, 0, 0]),
      ("aaabb", "cccca", [1, 0, 0, 0, 0]),
      ("aaabb", "acccc", [2, 0, 0, 0, 0]),
      ("aaabb", "acacc", [2, 0, 2, 0, 0]),
      ("aaabb", "acaca", [2, 1, 2, 0, 0]),
      ("bbaaa", "acaca", [0, 0, 2, 1, 2]),
      ("bbaaa", "ccaca", [0, 0, 2, 0, 2]),
    ]
    for case in cases:
      guess = case[0]
      solution = case[1]
      expected_diff_result = case[2]
      with self.subTest(name=(guess, solution)):
        diff_result = Differ.get_diff_result(guess, solution)
        self.assertEqual(diff_result, expected_diff_result)


  def test_throws_error_on_malformed_input(self):
    pass



if __name__ == '__main__':
    unittest.main()
