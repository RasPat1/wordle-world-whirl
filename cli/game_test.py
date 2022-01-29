from .game import Game

import unittest


class TestGameMethods(unittest.TestCase):

  def _GetDefaultGame(self):
    solution_corpus = {'cheese', 'clown', 'caret'}
    guess_corpus = {'saree', 'soare'}
    guess_count = 6

    return Game(solution_corpus, guess_corpus, guess_count)

  def testGameInstance(self):
    solution_corpus = {'cheese', 'clown', 'caret'}
    guess_corpus = {'saree', 'soare'}
    guess_count = 6
    self.assertIsInstance(
        Game(solution_corpus, guess_corpus, guess_count), Game)

  def testGameStoresInitConfig(self):
    solution_corpus = {'cheese', 'clown', 'caret'}
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
