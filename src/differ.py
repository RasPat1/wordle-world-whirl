from collections import defaultdict
from collections import Counter

class Differ:
  # Use a proper object for the diff.
  # I ended up with a slop show to handle that edge case with the multiple letters
    # 2 passes?
    # This awkward auiliary data structure for chars_counted(?)

  MATCH = 'm'
  CLOSE = 'c'
  ABSENT = 'a'

  def get_diff_result(guess, solution, solution_cache):
    cache_key = (guess, solution)
    if (cache_key in solution_cache):
      return solution_cache[cache_key]
    result = Differ.get_diff_result_impl(guess, solution)

    solution_cache[cache_key] = result

    return result

  # How similar are the 2 words?
  def get_diff_result_impl(guess, solution):
    """ Returns some type of match object? """
    result = [Differ.ABSENT, Differ.ABSENT, Differ.ABSENT, Differ.ABSENT, Differ.ABSENT]

    solution_char_counter = Counter(solution)
    assigned_char_counter = {}

    for index, guess_char in enumerate(guess):
      if not guess_char in assigned_char_counter:
        assigned_char_counter[guess_char] = 0

      if guess_char == solution[index]:
        result[index] = Differ.MATCH
        assigned_char_counter[guess_char] += 1
      else:
        result[index] = Differ.ABSENT

    # Todo: Lol this is clumsy.
    # We need information about the matches before we assign the "close" statuses so we use 2 passes.
    for index, guess_char in enumerate(guess):
      char_count_in_solution = solution_char_counter[guess_char]
      should_assign_char = assigned_char_counter[guess_char] < solution_char_counter[guess_char]
      if result[index] == Differ.ABSENT and guess_char in solution and should_assign_char:
        assigned_char_counter[guess_char] += 1
        result[index] = Differ.CLOSE

    return result
