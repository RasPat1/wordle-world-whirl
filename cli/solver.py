from src import wordle
from src import Reader
from src import CachedReducer
from src import Guesser
from src import ProfilerFactory
from src2 import MinimalPath


# Provides an API for a solver
#
# Usage
# Set Corpus
# Read Corpus
# loop
# Accept Guess Result Pairs
# Reduce Corpus
# Find and return "Best Guess"
# Await for more guess, result pairs
class Solver:

  def __init__(self):
    self.guess_results = set()
    self.solution_corpus = set()
    self.guess_corpus = set()

  def get_best_guess(self):
    # Both of these guesses should work.
    # print(f'mp result: {self.get_best_guess_mp()}')
    return self.get_best_guess_bf()

  def get_best_guess_bf(self):
    full_corpus = self.solution_corpus.union(self.guess_corpus)
    best_guesses = Guesser.get_best_guesses(self.solution_corpus, full_corpus, {
    }, {}, ProfilerFactory.getProfiler(False))
    print(best_guesses[0:100])
    if best_guesses:
      return best_guesses[0][0]
    else:
      return 'No possible solutions found!'

  # This uses the minimal path algorithm
  # The minimal path alg is expensive and does not support a solution corpus and guess corpus being separate.
  def get_best_guess_mp(self):
    # full_corpus = self.guess_corpus.union(self.solution_corpus)
    # result = MinimalPath.best_guess(full_corpus)

    result = MinimalPath.best_guess(self.solution_corpus)

    if result:
      print(result)
      return result[0]
    else:
      return 'No possible solutions found!'

  def reduce_corpus(self):
    for (guess, result) in self.guess_results:
      cr = CachedReducer(self.solution_corpus)
      self.solution_corpus = cr.reduce_corpus(guess, result)

  def add_guess_result(self, guess, result):
    self.guess_results.add((guess, result))
    # Check and fail on adding duplicates
    return True

  def use_full_corpus(self):
    self._load_corpus(wordle._SOLUTION_CORPUS_PATH, wordle._GUESS_CORPUS_PATH)

  def use_test_corpus(self):
    self._load_corpus(wordle._TEST_SOLUTION_PATH, wordle._TEST_GUESS_PATH)

  def _load_corpus(self, solution_corpus_path, guess_corpus_path):
    (self.solution_corpus, self.guess_corpus) = Reader.load_lists(
        solution_corpus_path, guess_corpus_path)
    self.solution_corpus = set(self.solution_corpus)
    self.guess_corpus = set(self.guess_corpus)

  def _update(self):
    pass
