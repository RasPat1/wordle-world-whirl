# Reads cleans and parses data from wordle dictionaries.
class Reader:

  def get_word_list(input_path):
    translation_table = {ord('"'): None, ord(','): ' ', ord('['): None, ord(']'): None}

    with open(input_path) as file:
      input = file.read()
      # Replace data structure characters and separate words by spaces.
      input = input.translate(translation_table)
      # Remove any excess new lines or spaces.
      input = input.strip()
      # Convert into array of words.
      input = input.split()

      return input
