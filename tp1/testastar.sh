#!/bin/bash

INPUT_FILE=$1

MAP=$2
TYPE=$3
HEURISTIC=$4

if [ $HEURISTIC == 1 ]; then
	HEURISTIC=manhattan
elif [ $HEURISTIC == 2 ]; then
	HEURISTIC=octile
fi

mkdir -p "output/stats/${TYPE}/"
mkdir -p "output/out/${TYPE}/"


while IFS=' ', read -r IX IY FX FY
do
	python3 ./source/main.py -f $MAP -ix $IX -iy $IY -fx $FX -fy $FY -a $TYPE -he $HEURISTIC -s "output/stats/${TYPE}/${TYPE}_${IX}_${IY}_${FX}_${FY}_${HEURISTIC}_stats" > "output/out/${TYPE}/${TYPE}_${IX}_${IY}_${FX}_${FY}_${HEURISTIC}_out"
done < "${INPUT_FILE}"
