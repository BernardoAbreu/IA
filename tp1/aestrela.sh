#!/bin/bash

# Script to run the A* search.

MAP=$1

IX=$2
IY=$3
FX=$4
FY=$5
HEURISTIC=$6

python3 ./source/main.py -f $MAP -ix $IX -iy $IY -fx $FX -fy $FY -a astar -h $HEURISTIC