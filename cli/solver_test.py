from .solver import Solver

import unittest


class TestSolverMethods(unittest.TestCase):

  def test_it_accepts_geuss_result(self):
    s = Solver()
    (guess, result) = ('ocean', 'absdf')

    self.assertEqual(s.add_guess_result(guess, result), True)


if __name__ == '__main__':
  unittest.main()
