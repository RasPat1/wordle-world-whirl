"""
A Game runner communicates between the user in the CLI and the game engine.

It boots up a game, accepts user inputs, sends guesses and responses, displays game stuff and whatever.

"""
from src import Reader
from .game import Game

_SOLUTION_CORPUS_PATH = "./data/wordle_dict_1"
_GUESS_CORPUS_PATH = "./data/wordle_dict_2"


class GameRunner:
  current_game = None

  def run():
    # Say hello to the user
    # Start a new Game
    # WHile the game is ongoing
      # Ask for a guess
      # Show a diff
    # Once the game is over tell them how they did
    # Ask if they want to play again.

    print("Hi! Do you want to play a game?")
    while True:
      game_over = GameRunner.play_game()
      if game_over:
        break

  def play_game():
    # What corpus should it use?
    solution_corpus = Reader.get_word_list(_SOLUTION_CORPUS_PATH)
    guess_corpus = Reader.get_word_list(_GUESS_CORPUS_PATH)

    game = Game(solution_corpus, guess_corpus)
    game.start()
    print("The game has started.")
    while game.state == Game.IN_PROGRESS:
      print("What's your guess?")
      guess = input()
      if guess == 'gtfo':
        return True
      diff = game.guess(guess)
      print("The diff:", diff)

    if game.result == Game.WIN:
      guess_count = len(game.guess_history)
      print(f'You won in {guess_count} guesses')
    else:
      print("You lost.")

    print("Do you wnat to play again? Y or N?")
    replay = input()
    if replay == 'Y':
      self.play_game()
    else:
      return True


if __name__ == '__main__':
  GameRunner.run()
