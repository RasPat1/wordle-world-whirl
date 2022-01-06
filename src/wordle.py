# Ugh I forgot how to write python.
# Wait I never knew how to write python....

import cProfile
import operator

from collections import defaultdict

from reader import Reader
from scorer import Scorer
from differ import Differ
from profiler import Profiler


_TEST_SOLUTION_PATH = "./data/test_dict_1"
_TEST_GUESS_PATH = "./data/test_dict_2"
_SOLUTION_CORPUS_PATH = "./data/wordle_dict_1"
_GUESS_CORPUS_PATH = "./data/wordle_dict_2"
_SMALL_SET = "./data/small_test_set_1"


class Wordle:
  profiler = None

  def process(self, solution_corpus_path, guess_corpus_path, output_count = -1):
    (solution_corpus, full_corpus) = Reader.load_lists(
      solution_corpus_path,
      guess_corpus_path
    )

    self.profiler.register_corpus(full_corpus)

    corpus_reduction_scores = defaultdict(list)
    cr_score_cache = {}
    diff_cache = {}
    self.profiler.register_cr_score_cache(cr_score_cache)
    self.profiler.register_diff_cache(diff_cache)

    # TODO: What if you switched the order of this loop?
    for solution in solution_corpus:
      for guess in full_corpus:
        diff_result = Differ.diff(guess, solution, diff_cache)

        cr_score_cache_key = (guess, ''.join(diff_result))

        if cr_score_cache_key in cr_score_cache:
          corpus_reduction_score = cr_score_cache[cr_score_cache_key]
        else:
          corpus_reduction_score = Scorer.get_corpus_reduction_score(guess, diff_result, solution_corpus, diff_cache, cr_score_cache)
        corpus_reduction_scores[guess].append(corpus_reduction_score)

        self.profiler.count_guess()

      self.profiler.count_guess()

    # Process the scores
    processed_scores = {word: Scorer.process_scores(result) for word, result in corpus_reduction_scores.items()}

    # Order the guesses from best to worst.
    ranked_scores = sorted(processed_scores.items(), key=lambda item: item[1], reverse=True)

    # Show the best guesses.
    print(ranked_scores[0:output_count])


  def start_profiler(self):
    self.profiler = Profiler()
    self.profiler.start()

  def stop_profiler(self):
    self.profiler.stop()


def main():
  # Default flags
  solution_corpus_path = _TEST_SOLUTION_PATH
  guess_corpus_path = _TEST_SOLUTION_PATH
  output_count = 20 # Set to -1 to print all entries
  # use_profiler = False

  w = Wordle()
  w.start_profiler()

  w.process(
    solution_corpus_path,
    guess_corpus_path,
    output_count
  )

  w.stop_profiler()


if __name__ == "__main__":
  cProfile.run('main()')
