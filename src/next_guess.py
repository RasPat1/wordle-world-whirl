from cached_reducer import CachedReducer
from reader import Reader
from profiler import ProfilerFactory
from guesser import Guesser
from guess_combinator import GuessCombinator


_TEST_SOLUTION_PATH = "./data/test_dict_1"
_TEST_GUESS_PATH = "./data/test_dict_2"
_SOLUTION_CORPUS_PATH = "./data/wordle_dict_1"
_GUESS_CORPUS_PATH = "./data/wordle_dict_2"
_MEDIUM_SET = "./data/medium_test_set_1"
_SMALL_SET = "./data/small_test_set_1"


class NextGuess:

  def process(solution_corpus, full_corpus):
    results = [
        # ('trice', 'acaam'),
        # ('salon', 'aaaca'),
    ]  # solution was gorge
    remaining_solution_corpus = solution_corpus
    remaining_full_corpus = full_corpus
    for (guess, distance) in results:
      remaining_solution_corpus = CachedReducer(
          remaining_solution_corpus).reduce_corpus(guess, distance)
      remaining_full_corpus = CachedReducer(
          remaining_full_corpus).reduce_corpus(guess, distance)
    print(remaining_solution_corpus[0:100])
    profiler = ProfilerFactory.getProfiler(False)
    best_guesses = GuessCombinator.process(
        remaining_solution_corpus, remaining_full_corpus, profiler, 1)
    # best_guesses = Guesser.get_best_guesses(
    #     remaining_solution_corpus, full_corpus, {}, {}, profiler)
    print(best_guesses[0:100])


def main():
  (solution_corpus,
   full_corpus) = Reader.load_lists(_TEST_SOLUTION_PATH, _TEST_GUESS_PATH)
  NextGuess.process(solution_corpus, full_corpus)


if __name__ == '__main__':
  main()
