import itertools

from differ import Differ
from scorer import Scorer
from cached_reducer import CachedReducer

from collections import defaultdict


class GuessCombinator:

  def process(solutions, full_corpus, cr_score_cache, diff_cache, profiler, guess_count=2):
    scores = defaultdict(list)
    cached_reducer = CachedReducer(full_corpus)
    solution_set = set(solutions)

    # get_one_hot = full_corpus

    for solution in solutions:
      for guesses in itertools.combinations(full_corpus, guess_count):
        corpus = solution_set
        for guess in guesses:
          diff = Differ.diff(guess, solution)
          partial_corpus = cached_reducer.reduce_corpus(guess, diff)
          corpus = corpus.intersection(partial_corpus)
        scores[guesses].append(len(corpus))
        profiler.count_guess()
      profiler.count_solution()

    processed_scores = {words: Scorer.process_scores(
        result) for words, result in scores.items()}
    ranked_scores = sorted(processed_scores.items(),
                           key=lambda item: item[1])
    # print(ranked_scores)
    return ranked_scores
