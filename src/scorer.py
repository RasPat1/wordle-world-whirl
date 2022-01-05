from statistics import mean
from differ import Differ

class Scorer:
  # How useful was this guess for the given soluiton?

  def get_score(guess, original_result, all_solutions, solution_cache, score_cache):
    score_cache_key = (guess, ''.join(original_result))
    if score_cache_key in score_cache:
      return score_cache[score_cache_key]

    score = Scorer.get_score_impl(guess, original_result, all_solutions, solution_cache)

    score_cache[score_cache_key] = score

    return score


  # Find how simliar the guess and solution are.
  # Compare the guess with every word in the solution dictionary.
  # If it has the same match result then it is a possible solution.
  # Get a point for ruling out a word.
  # Goal get a high score
  def get_score_impl(guess, original_result, all_solutions, solution_cache):
    score = 0

    for possible_solution in all_solutions:
      solution_cache_key = (guess, possible_solution)
      if solution_cache_key in solution_cache:
        match_result = solution_cache[solution_cache_key]
      else:
        match_result = Differ.get_diff_result(guess, possible_solution, solution_cache)
      if match_result != original_result:
        score += 1

    return score

  # How good is this guess in general?
  def process_scores(scores):
    return mean(scores)
