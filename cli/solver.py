from src import wordle
from src import Reader
from src import CachedReducer
from src import Guesser
from src import ProfilerFactory
from src2 import MinimalPath


# Provides an API for a solver
#
# Configure
#   Set Search Algorithm
#   Set Corpus
#
# Execute
#   Add Guess Result Pairs
#   Reduce Corpus
#   Find and return "Best Guess"
#   Repeat as needed.
class Solver:

  def __init__(self):
    self.guess_results = set()
    self.solution_corpus = set()
    self.guess_corpus = set()
    self.search_algorithm = self._get_best_guess_cr

  # Builder Fns
  ######################################
  def use_minimal_path_algorithm(self):
    self.search_algorithm = self._get_best_guess_mp

  def use_corpus_reduction_algorithm(self):
    self.search_algorithm = self._get_best_guess_cr

  def use_full_corpus(self):
    self._load_corpus(wordle._SOLUTION_CORPUS_PATH, wordle._GUESS_CORPUS_PATH)

  def use_test_corpus(self):
    self._load_corpus(wordle._TEST_SOLUTION_PATH, wordle._TEST_GUESS_PATH)
  ######################################

  def add_guess_result(self, guess, result):
    self.guess_results.add((guess, result))
    # Check and fail on adding duplicates
    return True

  def reduce_corpus(self):
    for (guess, result) in self.guess_results:
      cr = CachedReducer(self.solution_corpus)
      self.solution_corpus = cr.reduce_corpus(guess, result)

  def get_best_guess(self):
    return self.search_algorithm()

  # This uses the minimal path algorithm
  # The minimal path alg is expensive and does not support a solution corpus and guess corpus being separate.

  def _get_best_guess_mp(self):
    # full_corpus = self.guess_corpus.union(self.solution_corpus)
    # result = MinimalPath.best_guess(full_corpus)

    result = MinimalPath.best_guess(self.solution_corpus)

    if result:
      print(result)
      return result[0]
    else:
      return 'No possible solutions found!'

  def _get_best_guess_cr(self):
    full_corpus = self.solution_corpus.union(self.guess_corpus)
    best_guesses = Guesser.get_best_guesses(self.solution_corpus, full_corpus, {
    }, {}, ProfilerFactory.getProfiler(False))
    print(best_guesses[0:100])
    if best_guesses:
      return best_guesses[0][0]
    else:
      return 'No possible solutions found!'

  def _load_corpus(self, solution_corpus_path, guess_corpus_path):
    (self.solution_corpus, self.guess_corpus) = Reader.load_lists(
        solution_corpus_path, guess_corpus_path)
    self.solution_corpus = set(self.solution_corpus)
    self.guess_corpus = set(self.guess_corpus)
