from collections import defaultdict

from .scorer import Scorer
from .differ import Differ


class Guesser:

  def get_best_guesses(solution_corpus, full_corpus, cr_score_cache, diff_cache, profiler):
    corpus_reduction_scores = defaultdict(list)

    # Not elegant...
    if len(solution_corpus) == 1:
      return [(solution_corpus, 0)]

    for solution in solution_corpus:
      for guess in full_corpus:
        diff_result = Differ.diff(guess, solution)

        cr_score_cache_key = (guess, ''.join(diff_result))

        if cr_score_cache_key in cr_score_cache:
          corpus_reduction_score = cr_score_cache[cr_score_cache_key]
        else:
          corpus_reduction_score = Scorer.get_corpus_reduction_score(
              guess, diff_result, solution_corpus, diff_cache, cr_score_cache)
        corpus_reduction_scores[guess].append(corpus_reduction_score)

        profiler.count_guess()

      profiler.count_solution()

    # Process the scores
    processed_scores = {word: Scorer.process_scores(
        result) for word, result in corpus_reduction_scores.items()}

    # Order the guesses from best to worst.
    # Sort by highest corpus reduction score
    # Then sort by whther it's in the corpus or not.
    ranked_scores = sorted(processed_scores.items(),
                           key=lambda item: (item[1], item[0] in solution_corpus), reverse=True)

    return ranked_scores
