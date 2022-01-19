import sys
from .solver import Solver


def main():
  # Read an input
  guess, result = get_input_round()
  # Grab a wordle object initiated with the standard corpus
  solver = Solver()
  print(solver)

  # input is a word and a result
  # Send that to the solver
  # Get a reduced corpus and a best word
  # Tell best word and size of corpus
  # Repeat


def get_input_round():
  print("What was your guess?")
  guess = input()
  print(f'You guessed: {guess}')
  print('What was your result? Put a for absent, m for match and c for close')
  result = input()

  return (guess, result)


if __name__ == '__main__':
  main()
