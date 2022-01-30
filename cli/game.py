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
  GAME_STATES = [CONFIGURED, IN_PROGRESS, ENDED]

  WIN = 'win'
  LOSE = 'lose'
  GAME_RESULTS = [WIN, LOSE]

  def __init__(self, solution_corpus={}, guess_corpus={}, max_guesses=6):
    self.max_guesses = max_guesses
    self.solution_corpus = set(solution_corpus)
    self.guess_corpus = set(guess_corpus)

    self.guess_history = None
    self.secret_word = None
    self.state = Game.CONFIGURED
    self.result = None

  def start(self):
    self.guess_history = []
    self.secret_word = Game._GetRandomWord(self.solution_corpus)
    self.state = Game.IN_PROGRESS
    self.result = None

  # Nothing stopping the user from making the same guess twice.
  def guess(self, word):
    # Don't allow guesses if the game is not in progress
    if self.state != Game.IN_PROGRESS:
      return False

    # Don't guess if the word is invalid.
    if not self._IsValidGuess(word):
      return False

    # Store the guess in the history
    self.guess_history.append(word)
    self.update_game()

    # Generate diff between that word and the secret
    diff = Differ.diff(word, self.secret_word)

    return diff

  # Update the game based on the last guess.
  # Are you out of guesses? Did you win?
  def update_game(self):
    if self.state != Game.IN_PROGRESS:
      return

    if not self.guess_history:
      return

    # The last guess was correct!
    if self.guess_history[-1] == self.secret_word:
      self.state = Game.ENDED
      self.result = Game.WIN
    elif len(self.guess_history) >= self.max_guesses:
      self.state = Game.ENDED
      self.result = Game.LOSE

  def _IsValidGuess(self, word):
    return word in self.solution_corpus or word in self.guess_corpus

  def _GetRandomWord(corpus):
    return random.choice(list(corpus))

  # Debug methods
  # Show the size of both corpus after each guess
  # Get the secret word
