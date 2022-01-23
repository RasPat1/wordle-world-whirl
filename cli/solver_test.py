from .solver import Solver

import unittest


class TestSolverMethods(unittest.TestCase):

  def test_it_accepts_guess_result(self):
    s = Solver()
    (guess, result) = ('ocean', 'absdf')

    self.assertEqual(s.add_guess_result(guess, result), True)
    self.assertEqual(len(s.guess_results), 1)

  def test_can_use_full_dictionary(self):
    s = Solver()
    s.use_full_corpus()
    self.assertEqual(len(s.solution_corpus), 2315)
    self.assertEqual(len(s.guess_corpus), 12972)

  def test_can_use_test_dictionary(self):
    s = Solver()
    s.use_test_corpus()
    self.assertEqual(len(s.solution_corpus), 1349)
    self.assertEqual(len(s.guess_corpus), 1662)

  def test_can_reduce_corpus_when_no_guesses(self):
    s = Solver()
    s.solution_corpus = {'ocean', 'nopes'}
    s.guess_corpus = {'aaaaa', 'aaaab'}
    s.reduce_corpus()
    self.assertEqual(s.solution_corpus, {'ocean', 'nopes'})

  def test_can_reduce_corpus(self):
    s = Solver()
    s.solution_corpus = {'ocean', 'nopes'}
    s.guess_corpus = {'aaaaa', 'aaaab'}
    s.add_guess_result('ocean', 'mmmmm')
    s.reduce_corpus()
    self.assertEqual(s.solution_corpus, {'ocean'})

  def test_can_reduce_corpus_with_multiple_guesses(self):
    s = Solver()
    s.solution_corpus = {'forge', 'gorge', 'borge'}
    s.guess_corpus = {'aaaaa', 'aaaab'}
    s.add_guess_result('dorge', 'ammmm')
    s.add_guess_result('bbbbb', 'maaaa')
    s.reduce_corpus()
    self.assertEqual(s.solution_corpus, {'borge'})

  def test_gets_best_guess(self):
    s = Solver()
    s.solution_corpus = {'forge', 'gorge', 'borge'}
    s.guess_corpus = {'fggbe'}
    best_guess = s.get_best_guess()
    self.assertEqual(best_guess, 'fggbe')


if __name__ == '__main__':
  unittest.main()
