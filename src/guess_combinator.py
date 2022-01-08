import itertools

from differ import Differ
from scorer import Scorer

from collections import defaultdict


class GuessCombinator:

  def process(solutions, full_corpus, guess_count=2):
    scores = defaultdict(list)

    for solution in solutions:
      for guesses in itertools.combinations(full_corpus, guess_count):
        corpus = solutions
        for guess in guesses:
          diff = Differ.diff(guess, solution, {})
          corpus = Scorer.reduce_corpus(guess, diff, corpus)
        scores[guesses].append(len(corpus))

    processed_scores = {words: Scorer.process_scores(
        result) for words, result in scores.items()}
    ranked_scores = sorted(processed_scores.items(),
                           key=lambda item: item[1])
    # print(ranked_scores)
    return ranked_scores
