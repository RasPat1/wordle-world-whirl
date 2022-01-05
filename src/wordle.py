# Ugh I forgot how to write python.
# Wait I never knew how to write python....

from .reader import Reader

class Wordle:
  _TEST_SOLUTION_PATH = "./data/test_dict_1"
  _TEST_GUESS_PATH = "./data/test_dict_2"
  _SOLUTION_DICTIONARY_PATH = "./data/wordle_dict_1"
  _GUESS_DICTIONARY_PATH = "./data/wordle_dict_2"

  def main():
    solutions = Reader.get_word_list(Wordle._TEST_SOLUTION_PATH)
    guesses = Reader.get_word_list(Wordle._TEST_GUESS_PATH)
    print(solutions)
    print(guesses)


if __name__ == "__main__":
  main()
