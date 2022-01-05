from random import random
from statistics import mean
from .differ import Differ

class Scorer:
  # How useful was this guess for the given soluiton?
  def get_score(guess, solution, all_solutions):
    # Find how simliar the guess and solution are.
    # Compare the guess with every word in the solution dictionary.
    # If it has the same match result then it is a possible solution.
    # Get a point for ruling out a word.
    # Goal get a high score

    score = 0
    original_result = Differ.get_diff_result(guess, solution)

    for possible_solution in all_solutions:
      match_result = Differ.get_diff_result(guess, possible_solution)
      if match_result != original_result:
        score += 1
    return score

      # How good is this guess in general?
  def process_scores(scores):
    return mean(scores)
