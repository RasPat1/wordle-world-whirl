from statistics import mean
from differ import Differ

import functools


class Scorer:
  # How useful was this guess for the given soluiton?

  # When are you going to make a cache decorator?
  def get_corpus_reduction_score(guess, guess_solution_diff, all_solutions, diff_cache, cr_score_cache):
    score_cache_key = (guess, ''.join(guess_solution_diff))
    if score_cache_key in cr_score_cache:
      return cr_score_cache[score_cache_key]

    score = Scorer.get_corpus_reduction_score_impl(
        guess, guess_solution_diff, all_solutions, diff_cache)

    cr_score_cache[score_cache_key] = score

    return score

  # Find how simliar the guess and solution are.
  # Compare the guess with every word in the solution dictionary.
  # If it has the same match result then it is a possible solution.
  # Get a point for ruling out a word.
  # Goal get a high score

  def get_corpus_reduction_score_impl(guess, guess_solution_diff, solution_corpus, diff_cache):
    score = 0

    for possible_solution in solution_corpus:
      diff_cache_key = (guess, possible_solution)
      if diff_cache_key in diff_cache:
        match_result = diff_cache[diff_cache_key]
      else:
        match_result = Differ.diff(guess, possible_solution)

      if match_result != guess_solution_diff:
        score += 1

    return score

  def reduce_corpus(guess, guess_solution_diff, solution_corpus):
    reduced_corpus = []
    for possible_solution in solution_corpus:
      match_distance = Differ.diff(guess, possible_solution)
      if match_distance == guess_solution_diff:
        reduced_corpus.append(possible_solution)

    return reduced_corpus

  # How good is this guess in general?
  def process_scores(scores):
    return sum(scores)

  def process_scores_bin(bin_scores):
    actual_scores = [self.countSetBits(bin_score) for bin_score in bin_scores]
    return sum(scores)

  # We can just use a lookup table for this no?
  @functools.cache
  def countSetBits(binary_number):
    count = 0
    while (binary_number):
      binary_number &= (binary_number-1)
      count += 1

    return count


# Basically the cache for the diff is a diff for every pair of words. So that's dictionary size sq.
# For the corpus reducer it kind of is the same thing...
