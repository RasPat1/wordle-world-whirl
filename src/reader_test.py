from reader import Reader
import unittest

_ONE_WORD_PATH = "../data/unittest_data/one_word"
_ONE_WORD_2_PATH = "../data/unittest_data/one_word_2"
_DUPLICATE_WORD_PATH = "../data/unittest_data/duplicate_words"


class TestReaderMethods(unittest.TestCase):

  def test_read_solutions(self):
    solution_words = Reader.get_word_list(_ONE_WORD_PATH)
    self.assertListEqual(
        solution_words, ["words"])

  def test_makes_solution_unique(self):
    solution_words = Reader.get_word_list(_DUPLICATE_WORD_PATH)
    self.assertListEqual(
        solution_words, ["dupes"])

  def test_combines_solutions_and_guesses(self):
    _, corpus = Reader.load_lists(_ONE_WORD_PATH, _ONE_WORD_2_PATH)
    self.assertCountEqual(corpus, ["words", "dorks"])

  def test_dedupes_between_solutions_and_guesses(self):
    _, corpus = Reader.load_lists(_ONE_WORD_PATH, _DUPLICATE_WORD_PATH)
    self.assertCountEqual(corpus, ["words", "dupes"])


if __name__ == '__main__':
  unittest.main()
