# Reads cleans and parses data from wordle dictionaries.
class Reader:

  def load_lists(solution_corpus_path, guess_corpus_path):
    solution_corpus = Reader.get_word_list(solution_corpus_path)
    guess_corpus = Reader.get_word_list(guess_corpus_path)

    full_corpus = solution_corpus + guess_corpus
    full_corpus = Reader.unique(full_corpus)

    return (solution_corpus, full_corpus)

  def get_word_list(input_path):
    translation_table = {
        ord('"'): None,
        ord(','): ' ',
        ord('['): None,
        ord(']'): None
    }

    with open(input_path) as file:
      words = file.read()
      # Replace data structure characters and separate words by spaces.
      words = words.translate(translation_table)
      # Remove any excess new lines or spaces.
      words = words.strip()
      # Convert into array of words.
      words = words.split()

      unique_word_list = Reader.unique(words)

      return unique_word_list

  def unique(word_list):
    return list(set(word_list))
