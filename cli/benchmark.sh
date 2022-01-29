#! /bin/zsh

export PYTHONPATH="$(pwd);$(pwd)/src"
echo $PYTHONPATH
python -m src2.performance_tests
