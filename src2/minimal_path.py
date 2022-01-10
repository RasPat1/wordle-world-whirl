import functools
from collections import defaultdict
from collections import Counter


class Differ:
  def indexes_of(char, string):
    return [i for i, ltr in enumerate(string) if ltr == char]

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
      elif guess_char in solution and index in Differ.indexes_of(guess_char, solution):
        located_characters[guess_char].append(index)
        char_count[guess_char] += 1
        # Now remove from unlocated characers if necessary?
        # Upgrade to located char kinda thing
      elif guess_char in solution and not index in Differ.indexes_of(guess_char, solution) and char_count[guess_char] < solution_char_counter[guess_char]:
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


class Filter:
  # @functools.cache
  def filter(guess, solution, corpus):
    reduced_corpus = []
    baseline_diff = Differ.diff(guess, solution)

    for candidate in corpus:
      candidate_diff = Differ.diff(guess, candidate)
      if candidate_diff == baseline_diff:
        reduced_corpus.append(candidate)

    return reduced_corpus


class MinimalPath:
  def best_guess(corpus):
    if len(corpus) == 1:
      return (corpus[0], 1)

    # we coudl refactor this to corpus[0] and remvoe the base case.
    best_guess = '___'
    best_guess_path_len = len(corpus)

    # Over a corpus we have a best guess. Let's find it.
    # That guess is the one that leads to the shortest average path.
    for guess in corpus:
      total_path_len = 0
      # over all solutions we have an average path length
      for solution in corpus:
        reduced_corpus = Filter.filter(guess, solution, corpus)

        # Shouldn't happen right now since all guesses are in the corpus and guessing them must at least exclude themselves.
        # Keep in mind when you can guess non-solutions.
        if len(corpus) == len(reduced_corpus):
          pass

        (reduced_corpus_best_guess, guess_len) = MinimalPath.best_guess(reduced_corpus)
        total_path_len += guess_len
      average_path_len = total_path_len / len(corpus)
      if average_path_len < best_guess_path_len:
        best_guess_path_len = average_path_len
        best_guess = guess

    return (best_guess, 1 + best_guess_path_len)


def main():
  MinimalPath.process()


if __name__ == "__main__":
  main()
