import functools
from collections import defaultdict
from collections import Counter
from .differ_old import Differ
from .cached_reducer_old import CachedReducer


class Filter:
  # @functools.cache
  def filter(guess, solution, corpus):
    reduced_corpus = []
    baseline_diff = Differ.diff(guess, solution)

    for candidate in corpus:
      candidate_diff = Differ.diff(guess, candidate)
      if candidate_diff == baseline_diff:
        reduced_corpus.append(candidate)

    return reduced_corpus


class MinimalPath:
  def best_guess(corpus):
    corpus = list(corpus)
    if len(corpus) == 1:
      return (corpus[0], [corpus[0]], 0)

    # We could refactor this to corpus[0] and remove the base case.
    best_guess = ''
    best_guess_path = []
    best_guess_avg_path_len = len(corpus)

    # Over a corpus we have a best guess. Let's find it.
    # That guess is the one that leads to the shortest average path.
    cr = CachedReducer(corpus)
    for guess in corpus:
      total_path_len = 0
      # over all solutions we have an average path length
      for solution in corpus:
        reduced_corpus = Filter.filter(guess, solution, corpus)

        # Shouldn't happen right now since all guesses are in the corpus and guessing them must at least exclude themselves, but relevant when
        # when you can guess non-solutions.
        if len(corpus) == len(reduced_corpus):
          pass

        (reduced_corpus_best_guess, best_guess_path,
         guess_len) = MinimalPath.best_guess(reduced_corpus)
        total_path_len += guess_len
      average_path_len = total_path_len / len(corpus)
      if average_path_len < best_guess_avg_path_len:
        best_guess_avg_path_len = average_path_len
        best_guess_path = best_guess_path
        best_guess = guess

    result = (best_guess, [best_guess] + best_guess_path,
              1 + best_guess_avg_path_len)

    return result


def main():
  MinimalPath.best_guess()


if __name__ == "__main__":
  main()
