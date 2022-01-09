# Ugh I forgot how to write python.
# Wait I never knew how to write python....

import cProfile
import operator

from datetime import datetime

from guesser import Guesser
from guess_combinator import GuessCombinator
from reader import Reader
from profiler import ProfilerFactory


_TEST_SOLUTION_PATH = "./data/test_dict_1"
_TEST_GUESS_PATH = "./data/test_dict_2"
_SOLUTION_CORPUS_PATH = "./data/wordle_dict_1"
_GUESS_CORPUS_PATH = "./data/wordle_dict_2"
_MEDIUM_SET = "./data/medium_test_set_1"
_SMALL_SET = "./data/small_test_set_1"


class Wordle:
  def __init__(self, solution_corpus_path, guess_corpus_path, output_count=-1, use_profiler=False, write_to_file=False):
    self.solution_corpus_path = solution_corpus_path
    self.guess_corpus_path = guess_corpus_path
    self.output_count = output_count
    self.profiler = ProfilerFactory.getProfiler(use_profiler)
    self.write_to_file = write_to_file

  def process(self):
    try:
      self.profiler.start()
      (solution_corpus, full_corpus) = Reader.load_lists(
          self.solution_corpus_path,
          self.guess_corpus_path
      )

      self.profiler.register_corpus(full_corpus)

      cr_score_cache = {}
      diff_cache = {}

      self.profiler.register_cr_score_cache(cr_score_cache)
      self.profiler.register_diff_cache(diff_cache)

      ranked_scores = GuessCombinator.process(
          solution_corpus, full_corpus, cr_score_cache, diff_cache, self.profiler, 2)
      # ranked_scores = Guesser.get_best_guesses(
      #     solution_corpus, full_corpus, cr_score_cache, diff_cache, self.profiler)

      # Show the best guesses.
      self.write_or_print_results(ranked_scores[0:self.output_count])

    finally:
      self.profiler.stop()

  def write_or_print_results(self, results):
    results = [f'\n{str(result)}' for result in results]
    results.insert(0, self.profiler._status_string())
    if self.write_to_file:
      try:
        output_filename = "results/results--" + str(datetime.now())
        output_file = open(output_filename, 'w')
        output_file.writelines(results)
      finally:
        output_file.close()
    else:
      print(''.join(results))


def main():
  # Default flags
  solution_corpus_path = _TEST_SOLUTION_PATH
  guess_corpus_path = _TEST_GUESS_PATH
  output_count = -1  # Set to -1 to print all entries
  use_profiler = True
  write_to_file = True

  w = Wordle(solution_corpus_path,
             guess_corpus_path,
             output_count, use_profiler, write_to_file)

  w.process()


if __name__ == "__main__":
  cProfile.run('main()')
