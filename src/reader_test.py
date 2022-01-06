from .reader import Reader
import unittest

_TEST_SOLUTION_PATH = "./data/test_dict_1"
_TEST_GUESS_PATH = "./data/test_dict_2"


class TestReaderMethods(unittest.TestCase):

  def test_read_solutions(self):
    solution_words = Reader.get_word_list(_TEST_SOLUTION_PATH)
    self.assertEqual(
        solution_words, ["cigar", "rebut", "sissy", "humph", "awake", "blush", "focal"])

  def test_read_guesses(self):
    guess_words = Reader.get_word_list(_TEST_GUESS_PATH)
    self.assertEqual(guess_words, ["aahed", "aalii", "aargh", "aarti", "abaca"])


if __name__ == '__main__':
  unittest.main()
