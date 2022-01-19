from src import wordle


# Provides an API for a solver
class Solver:
  def get_best_guess(self):
    pass

  def add_guess_result(self, guess, result):
    return True

  def use_full_dictionary(self):
    pass

  def use_test_dictionary(self):
    pass

  def _update(self):
    pass
