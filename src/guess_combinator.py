import itertools

from differ import Differ
from scorer import Scorer
from cached_reducer import CachedReducer
from bit_counter import BitCounter

from collections import defaultdict


class GuessCombinator:
  MASK_SIZE = 13  # Because... Resaons.

  def process(solutions, full_corpus, cr_score_cache, diff_cache, profiler, guess_count=2):

    scores = defaultdict(lambda: 0)

    solution_set = set(solutions)
    corpus_rep = (0b1 << len(solutions) + 1) - 1

    cached_reducer = CachedReducer(full_corpus)
    bc = BitCounter(GuessCombinator.MASK_SIZE)

    profiler.register_cached_fn('countSetBits', bc.countSetBits)
    profiler.register_cached_fn('countBitsLoop', bc.count_set_bits_loop)
    profiler.register_cached_fn(
        'reduce_corpus_bin', cached_reducer.reduce_corpus_bin)
    profiler.register_cached_fn(
        'reduce_corpus', cached_reducer.reduce_corpus)
    profiler.register_cached_fn('Differ', Differ.diff)

    for solution in solutions:
      for guesses in itertools.combinations(full_corpus, guess_count):
        corpus_copy = corpus_rep
        reduced_corpus = solution_set
        for guess in guesses:
          diff = Differ.diff(guess, solution)
          partial_corpus_rep = cached_reducer.reduce_corpus_bin(guess, diff)
          corpus_copy = partial_corpus_rep & corpus_copy
          # partial_corpus = cached_reducer.reduce_corpus(guess, diff)
          # reduced_corpus = partial_corpus.intersection(reduced_corpus)

        # Subtract 1 for buffer bit.
        final_corpus_length = bc.count_set_bits_loop(corpus_copy) - 1
        scores[guesses] += final_corpus_length
        # scores[guesses] += len(reduced_corpus)
        # profiler.count_guess()
      profiler.count_solution()

    # processed_scores = {words: Scorer.process_scores(
    #     result) for words, result in scores.items()}
    ranked_scores = sorted(scores.items(),
                           key=lambda item: item[1])
    # print(ranked_scores)
    return ranked_scores
