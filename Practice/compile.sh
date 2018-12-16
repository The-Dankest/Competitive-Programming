#!/usr/bin/env bash
if [ $# -eq 2 ]; then
    echo "arguments are wrong lol"
else
    echo "compiling...."
    g++ -Wall -Wextra -std=c++11 -O2 -o$2 $1
fi