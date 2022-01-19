#! /bin/zsh

export PYTHONPATH="$(pwd);$(pwd)/src"
echo $PYTHONPATH
python -m unittest cli.solver_test
