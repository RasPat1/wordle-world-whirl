import functools

from .differ import Differ


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

  @functools.cache
  def reduce_corpus_bin(self, guess, diff):
    corpus_rep = 0b1
    for possible_solution in self.corpus:
      match_distance = Differ.diff(guess, possible_solution)
      if match_distance == diff:
        corpus_rep = (corpus_rep << 1) + 1
      else:
        corpus_rep = corpus_rep << 1

    return corpus_rep
