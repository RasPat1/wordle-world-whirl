from collections import defaultdict
from collections import Counter

class Differ:
  # Use a proper object for the diff.
  # Enums would be more readable than the ints.
  # I ended up with a slop show to handle that edge case with the multiple letters
    # 2 passes?
    # This awkward auiliary data structure for chars_counted(?)
    # The char counting is correct but the logic is indirect. This can be expressed more directly.

  # How similar are the 2 words?
  def get_diff_result(guess, solution, solution_cache):
    """ Returns some type of match object? """
    cache_key = (guess, solution)
    if (cache_key in solution_cache):
      return solution_cache[cache_key]

    result = [0,0,0,0,0]

    chars_counted = {}

    for index, guess_char in enumerate(guess):
      if not guess_char in chars_counted:
        chars_counted[guess_char] = 0

      if guess_char == solution[index]:
        chars_counted[guess_char] += 1
        result[index] = 2
      else:
       result[index] = 0

    # Do the "close" scores after establishing the exact letter match/mismatches.
    for index, guess_char in enumerate(guess):
      char_count_in_solution = solution.count(guess_char)
      # Todo: Lol this is clumsy.
      more_instances_in_guess_than_solution = chars_counted[guess_char] >= char_count_in_solution

      if result[index] == 0 and guess_char in solution and not more_instances_in_guess_than_solution:
        chars_counted[guess_char] += 1
        result[index] = 1

    solution_cache[cache_key] = result

    return result
