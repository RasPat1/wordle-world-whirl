# Ugh I forgot how to write python.
# Wait I never knew how to write python....

import cProfile
import operator

from collections import defaultdict
from datetime import datetime

from reader import Reader
from scorer import Scorer
from differ import Differ
from timer import RepeatTimer

def print_time():
  now = datetime.now()

  current_time = now.strftime("%H:%M:%S")
  print("Solutions Searched: ", Wordle.solution_count, current_time)
  if Wordle.solution_count < 100:
    print("Guesses Searched: ", Wordle.guess_count)

class Wordle:
  _TEST_SOLUTION_PATH = "./data/test_dict_1"
  _TEST_GUESS_PATH = "./data/test_dict_2"
  _SOLUTION_DICTIONARY_PATH = "./data/wordle_dict_1"
  _GUESS_DICTIONARY_PATH = "./data/wordle_dict_2"

  _SMALL_SET = "./data/small_test_set_1"

  solution_count = 0
  guess_count = 0

  def main():
    all_solutions = Reader.get_word_list(Wordle._SOLUTION_DICTIONARY_PATH)
    all_guesses = Reader.get_word_list(Wordle._GUESS_DICTIONARY_PATH)

    # solutions and guesses are both guessable
    dictionary = all_solutions + all_guesses

    # Make sure they are unique.
    dictionary = list(set(dictionary))

    print("Dictionary Size:", len(dictionary))
    scores = defaultdict(list)
    solution_cache = {}
    score_cache = {}

    timer = RepeatTimer(5, print_time)
    timer.start()

    for solution in all_solutions:
      for guess in dictionary:
        match = Differ.get_diff_result(guess, solution, solution_cache)

        score_cache_key = (guess, ''.join(match))
        if score_cache_key in score_cache:
          score = score_cache[score_cache_key]
        else:
          score = Scorer.get_score(guess, match, all_solutions, solution_cache, score_cache)
        scores[guess].append(score)
        Wordle.guess_count += 1
      Wordle.guess_count = 0
      Wordle.solution_count +=1

    timer.cancel()

    # Process the scores
    processed_scores = {word: Scorer.process_scores(result) for word, result in scores.items()}

    # Order the guesses from best to worst.
    ranked_scores = sorted(processed_scores.items(), key=lambda item: item[1], reverse=True)

    # Show the best guesses.
    display_count = 20
    print(ranked_scores[0:display_count])
    print("Score Cache Size:", len(score_cache))
    print("Solution Cache Size:", len(solution_cache))


if __name__ == "__main__":
  cProfile.run('Wordle.main()')
