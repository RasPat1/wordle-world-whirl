#! /bin/zsh

export PYTHONPATH="$(pwd);$(pwd)/src"
echo $PYTHONPATH
python -m cli.game_runner
