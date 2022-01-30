from .game import Game

import unittest
import random
from src import Differ


class TestGameMethods(unittest.TestCase):

  def _GetDefaultGame(self):
    solution_corpus = {'chess', 'clown', 'caret'}
    guess_corpus = {'saree', 'soare'}
    guess_count = 6

    return Game(solution_corpus, guess_corpus, guess_count)

  def testGameInstance(self):
    solution_corpus = {'chess', 'clown', 'caret'}
    guess_corpus = {'saree', 'soare'}
    guess_count = 6
    self.assertIsInstance(
        Game(solution_corpus, guess_corpus, guess_count), Game)

  def testGameStoresInitConfig(self):
    solution_corpus = {'chess', 'clown', 'caret'}
    guess_corpus = {'saree', 'soare'}
    guess_count = 6

    game = Game(solution_corpus, guess_corpus, guess_count)

    self.assertEqual(game.max_guesses, guess_count)
    self.assertEqual(game.solution_corpus, solution_corpus)
    self.assertEqual(game.guess_corpus, guess_corpus)
    self.assertEqual(game.state, Game.CONFIGURED)

  def testGameStartsCorrectly(self):
    game = self._GetDefaultGame()
    game.start()

    self.assertEqual(game.guess_history, [])
    self.assertIn(game.secret_word, game.solution_corpus)
    self.assertEqual(game.state, Game.IN_PROGRESS)

  def testGetsRandomWordFromSolutionCorpus(self):
    game = self._GetDefaultGame()
    game.start()

    random_words = set()

    # After n^n iterations we should recover the original corpus with high probability.
    solution_corpus_size = len(game.solution_corpus)
    iterations = solution_corpus_size**solution_corpus_size

    for _ in range(iterations):
      game.start()
      random_words.add(game.secret_word)

    self.assertEqual(random_words, game.solution_corpus)

  def testDoesNotGetWordsFromGuessCorpus(self):
    game = self._GetDefaultGame()

    random_words = set()

    solution_corpus_size = len(game.solution_corpus)
    iterations = solution_corpus_size**solution_corpus_size

    for _ in range(iterations):
      game.start()
      random_words.add(game.secret_word)

    overlapping_words = game.guess_corpus.intersection(random_words)
    self.assertEqual(overlapping_words, set())

  def testCanGuessWords(self):
    game = self._GetDefaultGame()
    game.start()
    word = Game._GetRandomWord(game.solution_corpus)

    self.assertIsInstance(game.guess(word), str)

  def testGuessesFailOnBadWords(self):
    game = self._GetDefaultGame()
    game.start()
    self.assertEqual(game.guess("fakeword"), False)

  def testReturnsCorrectDiff(self):
    game = self._GetDefaultGame()
    game.start()
    word = Game._GetRandomWord(game.guess_corpus)

    # Ooops. Use dependency injection to avoid this.
    # Or python mocking.
    expected_diff = Differ.diff(word, game.secret_word)
    self.assertEqual(game.guess(word), expected_diff)

  def testStoresGuessesInHistory(self):
    game = self._GetDefaultGame()
    game.start()
    word = Game._GetRandomWord(game.guess_corpus)
    game.guess(word)

    self.assertListEqual(game.guess_history, [word])

  def testCanNotGuessIfGameIsNotStarted(self):
    game = self._GetDefaultGame()
    word = Game._GetRandomWord(game.guess_corpus)

    self.assertEqual(game.guess(word), False)

  def testCanNotGuessIfGameIsEnded(self):
    game = self._GetDefaultGame()
    game.state = Game.ENDED
    word = Game._GetRandomWord(game.guess_corpus)

    self.assertEqual(game.guess(word), False)

  def testGameResultIsWinWhenSecretWordIsGuessed(self):
    game = self._GetDefaultGame()
    game.start()
    word = game.secret_word
    game.guess(word)

    self.assertEqual(game.state, Game.ENDED)
    self.assertEqual(game.result, Game.WIN)

  def testGameResultIsLoseWhenGuessCountIsExceeded(self):
    game = self._GetDefaultGame()
    game.start()
    word = Game._GetRandomWord(game.guess_corpus)
    for _ in range(game.max_guesses):
      game.guess(word)

    self.assertEqual(game.state, Game.ENDED)
    self.assertEqual(game.result, Game.LOSE)
