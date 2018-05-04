#!/bin/bash

# Script to run the Uniform cost search.

MAP=$1

IX=$2
IY=$3
FX=$4
FY=$5

python3 ./source/main.py -f $MAP -ix $IX -iy $IY -fx $FX -fy $FY -a ucs
