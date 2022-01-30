import functools
import time

from collections import defaultdict
from collections import Counter
from .differ_old import Differ


class Filter:

  # You could chunk the corpus. The filter process is a linear combination.
  # We can cache guess, solution, corpus[0:n] and g,s,corpus[n:2n] etc. Incrase the chance of cache hits. And you may be able to do it in a smart way to maximize the chance of cache hits.
  @functools.cache
  def cached_filter(guess, solution, corpus_str):
    # print(guess, solution, corpus_str)
    baseline_diff = Differ.diff(guess, solution)
    return Filter.cached_filter_with_diff(guess, baseline_diff, corpus_str)

  @functools.cache
  def cached_filter_with_diff(guess, baseline_diff, corpus_str):
    corpus = corpus_str.split(',')
    reduced_corpus = []

    for candidate in corpus:
      candidate_diff = Differ.diff(guess, candidate)
      if candidate_diff == baseline_diff:
        reduced_corpus.append(candidate)

    return reduced_corpus

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
  corpus_sizes = defaultdict(int)

  @functools.cache
  # Adding the cache sped it up by 100x for a corpus of 50 words.
  def cached_best_guess(corpus_str):
    corpus = corpus_str.split(',')
    return MinimalPath.best_guess(corpus)

  def best_guess(corpus):
    if len(corpus) == 1:
      return (corpus[0], [corpus[0]], 0)

    # We could refactor this to corpus[0] and remove the base case.
    best_guess = ''
    best_guess_path = []
    best_guess_avg_path_len = len(corpus)

    corpus_str = ','.join(corpus)

    # Over a corpus we have a best guess. Let's find it.
    # That guess is the one that leads to the shortest average path.
    for guess in corpus:
      total_path_len = 0
      # over all solutions we have an average path length
      for solution in corpus:
        reduced_corpus = Filter.cached_filter(guess, solution, corpus_str)

        reduced_corpus_str = ','.join(reduced_corpus)
        (reduced_corpus_best_guess, guess_path,
         guess_len) = MinimalPath.cached_best_guess(reduced_corpus_str)

        total_path_len += guess_len

      average_path_len = total_path_len / len(corpus)
      if average_path_len < best_guess_avg_path_len:
        best_guess_avg_path_len = average_path_len
        best_guess_path = guess_path
        best_guess = guess

    result = (best_guess, [best_guess] + best_guess_path,
              1 + best_guess_avg_path_len)
    return result


def main():
  MinimalPath.best_guess()


if __name__ == "__main__":
  main()
