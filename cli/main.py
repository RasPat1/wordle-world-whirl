import sys
from .solver import Solver


def main():
  solver = Solver()
  solver.use_only_solution_corpus()
  # solver.use_minimal_path_algorithm()

  while True:
    print(f'Corpus Size: {len(solver.solution_corpus)}')
    print(f'Guess Size: {len(solver.guess_corpus)}')

    (guess, result) = get_input_round()

    if guess == 'exit':
      break

    solver.add_guess_result(guess, result)
    solver.reduce_corpus()

    print(f'Best Guess {solver.get_best_guess()}')


def get_input_round():
  print("What was your guess?")
  guess = input()
  print(f'You guessed: {guess}')
  print('What was your result? Put a for absent, m for match and c for close')
  result = input()

  return (guess, result)


if __name__ == '__main__':
  main()
