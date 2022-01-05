# Ugh I forgot how to write python.
# Wait I never knew how to write python....

import operator
from collections import defaultdict

from .reader import Reader
from .scorer import Scorer

class Wordle:
  _TEST_SOLUTION_PATH = "./data/test_dict_1"
  _TEST_GUESS_PATH = "./data/test_dict_2"
  _SOLUTION_DICTIONARY_PATH = "./data/wordle_dict_1"
  _GUESS_DICTIONARY_PATH = "./data/wordle_dict_2"

  def main():
    all_solutions = Reader.get_word_list(Wordle._SOLUTION_DICTIONARY_PATH)
    all_guesses = Reader.get_word_list(Wordle._GUESS_DICTIONARY_PATH)

    # solutions and guesses are both guessable
    dictionary = all_solutions + all_guesses

    scores = defaultdict(list)

    for solution in all_solutions:
      for guess in dictionary:
        score = Scorer.get_score(guess, solution, all_solutions)
        scores[guess].append(score)

    # Process the scores
    processed_scores = {word: Scorer.process_scores(result) for word, result in scores.items()}

    # Order the guesses from best to worst.
    ranked_scores = sorted(processed_scores.items(), key=lambda item: item[1], reverse=True)

    # Show the best guesses.
    display_count = 20
    print(ranked_scores[0:display_count])


if __name__ == "__main__":
  main()
