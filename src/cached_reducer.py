import functools

from differ import Differ


class CachedReducer:
  def __init__(self, corpus):
    self.corpus = corpus

  @functools.cache
  def reduce_corpus(self, guess, diff):
    reduced_corpus = set()
    for possible_solution in self.corpus:
      match_distance = Differ.diff(guess, possible_solution)
      if match_distance == diff:
        reduced_corpus.add(possible_solution)

    return reduced_corpus
