# Ugh I forgot how to write python.
# Wait I never knew how to write python....

import operator
from random import random
from statistics import mean
from collections import defaultdict

from .reader import Reader


class Wordle:
  _TEST_SOLUTION_PATH = "./data/test_dict_1"
  _TEST_GUESS_PATH = "./data/test_dict_2"
  _SOLUTION_DICTIONARY_PATH = "./data/wordle_dict_1"
  _GUESS_DICTIONARY_PATH = "./data/wordle_dict_2"

  # How useful was this guess for the given soluiton?
  def get_score(guess, solution, dictionary):
    return random()

  # How good is this guess in general?
  def process_scores(scores):
    return mean(scores)

  def main():
    solutions = Reader.get_word_list(Wordle._TEST_SOLUTION_PATH)
    guesses = Reader.get_word_list(Wordle._TEST_GUESS_PATH)

    # solutions and guesses are both guessable
    dictionary = solutions + guesses

    scores = defaultdict(list)

    for solution in solutions:
      for guess in dictionary:
        score = Wordle.get_score(guess, solution, dictionary)
        scores[guess].append(score)


    # Process the scores
    processed_scores = {word: Wordle.process_scores(result) for word, result in scores.items()}

    # Best Score?
    ranked_scores = sorted(processed_scores.items(), key=operator.itemgetter(1))
    show = 2 # Show the top 5
    print(ranked_scores[0:show])



if __name__ == "__main__":
  main()
