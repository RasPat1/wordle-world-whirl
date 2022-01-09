from cached_reducer import CachedReducer
from reader import Reader


class NextGuess:

  def process(solution_corpus):
    results = [
        ('trice', 'acaam'),
        ('salon', 'aaaca')
    ]
    remaining_corpus = solution_corpus
    for (guess, distance) in results:
      remaining_corpus = CachedReducer(
          remaining_corpus).reduce_corpus(guess, distance)
    print(remaining_corpus)


if __name__ == '__main__':
  path = "./data/wordle_dict_1"
  word_list = Reader.get_word_list(path)
  NextGuess.process(word_list)
