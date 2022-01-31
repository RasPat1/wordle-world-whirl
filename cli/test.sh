#! /bin/zsh

export PYTHONPATH="$(pwd);$(pwd)/src"
echo $PYTHONPATH
python -m unittest cli.game_runner_test
