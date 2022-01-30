"""
A game holds a corpus of allowed guesses and allowed solutions, a secret word, and a guess history.

A game is initialized with a guess and solution corpus, and a max number of guesses.

At the start of the game, the game object randomly selects a word from the solution corpus.

If the user guesses the secret word the user wins, if the user does not guess the secret word in the allotted number of guesses the user loses.

After each user guess the game returns a "diff" between their guess and the secret word.

"""

import random
from src import Differ


class Game:
  CONFIGURED = 'configured'
  IN_PROGRESS = 'in_progress'
  ENDED = 'ended'
  GAME_STATES = [
      CONFIGURED, IN_PROGRESS, ENDED
  ]

  def __init__(self, solution_corpus={}, guess_corpus={}, max_guesses=6):
    self.max_guesses = max_guesses
    self.solution_corpus = set(solution_corpus)
    self.guess_corpus = set(guess_corpus)

    self.guess_history = None
    self.secret_word = None
    self.state = Game.CONFIGURED

  def start(self):
    self.guess_history = []
    self.secret_word = Game._GetRandomWord(self.solution_corpus)
    self.state = Game.IN_PROGRESS

  def guess(self, word):
    # Don't allow guesses if the game is not in progress
    if self.state != Game.IN_PROGRESS:
      return False

    # Don't guess if the word is invalid.
    if not self._IsValidGuess(word):
      return False

    # Store the guess in the history
    self.guess_history.append(word)

    # Generate diff between that word and the secret
    diff = Differ.diff(word, self.secret_word)

    return diff

  # Check if the user wins or losses
  def is_game_over(self):
    # If the user is out of guesses and they haven't guessed
    # the word they lose.
    # If they've guessed the word they win
    # If they haven't guessed the word and still have guesses remaining the game is still ongoing.
    # Update the game state to be completed.
    pass

  def _IsValidGuess(self, word):
    return word in self.solution_corpus or word in self.guess_corpus

  def _GetRandomWord(corpus):
    return random.choice(list(corpus))

  # Debug methods
  # Show the size of both corpus after each guess
  # Get the secret word
