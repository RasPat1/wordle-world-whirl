from statistics import mean
from differ import Differ


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

  def get_corpus_reduction_score_impl(guess, guess_solution_diff, all_solutions, diff_cache):
    score = 0

    for possible_solution in all_solutions:
      diff_cache_key = (guess, possible_solution)
      if diff_cache_key in diff_cache:
        match_result = diff_cache[diff_cache_key]
      else:
        match_result = Differ.diff(guess, possible_solution, diff_cache)
      if match_result != guess_solution_diff:
        score += 1

    return score

  # How good is this guess in general?
  def process_scores(scores):
    return mean(scores)
