"""
A game holds a corpus of allowed guesses and allowed solutions, a secret word, and a guess history.

A game is initialized with a guess and solution corpus, and a max number of guesses.

At the start of the game, the game object randomly selects a word from the solution corpus.

If the user guesses the secret word the user wins, if the user does not guess the secret word in the allotted number of guesses the user loses.

After each user guess the game returns a "diff" between their guess and the secret word.

"""

import random


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
    self.secret_word = random.choice(list(self.solution_corpus))
    self.state = Game.IN_PROGRESS

  def guess(self, word):
    # If the word is not valid return with a fail state

    # Store the guess in the history
    # Generate diff between that word and the secret
    # Check if the user wins or losses
    # Return a diff, a win status, or a lose status
    pass

  # Debug methods
  # Show the size of both corpus after each guess
  # Get the secret word
