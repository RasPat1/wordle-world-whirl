
class Differ2:
  def indexes_of(char, string):
    return [i for i, ltr in enumerate(string) if ltr == char]

  # This is dumb just use your old differ.
  def diff(guess, solution):
    # A word is a list of characters and their positions
    # {char: [positions]}
    # A diff is known character positions, known absent characters, charac
    # Diff is excluded characters, Included Characters @ location, Included Characeter @ not location

    excluded_characters = set()
    char_count = defaultdict(lambda: 0)
    solution_char_counter = Counter(solution)
    located_characters = defaultdict(list)
    unlocated_characters = defaultdict(list)

    for index, guess_char in enumerate(guess):
      if not guess_char in solution:
        excluded_characters.add(guess_char)
        char_count[guess_char] = 0
      elif guess_char in solution and index in Differ2.indexes_of(guess_char, solution):
        located_characters[guess_char].append(index)
        char_count[guess_char] += 1
        # Now remove from unlocated characers if necessary?
        # Upgrade to located char kinda thing
      elif guess_char in solution and not index in Differ2.indexes_of(guess_char, solution) and char_count[guess_char] < solution_char_counter[guess_char]:
        unlocated_characters[guess_char].append(index)
        char_count[guess_char] += 1
      else:
        print("This is broken or we hit that edge case. Manually check it.")

    return (excluded_characters, located_characters, unlocated_characters)

    # TOdo
    # Figure out how to handle those multiletter edge cases.
    # My old code essentially gave us hte number of occurences. That was extra info. This might not provide that.
    # This is lightly wrong i think.

    # TODO
    # I need to test the actual wordle app to see what it does on the multiletter situation.  Which one does it light up?

  def equal(diff1, diff2):
    # we can actually just use ==.
    # Wow pyhton is amazing.
    return diff1 == diff2
