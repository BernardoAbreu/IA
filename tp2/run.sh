#!/bin/bash

PA=$HOME'/IA/tp2'
TEST_VERSION=2
DATA=(pacmaze-01-tiny.txt pacmaze-02-mid-sparse.txt pacmaze-03-tricky.txt)
SUBDIRS=(0.2 0.3 0.5 0.7 0.9)
OUT=tests

ALPHA=0.2
DISCOUNT=0.9
N=100000
EPSILON=0.2


while getopts 'd:v:o:n:s:h' opt ; do
  case $opt in
    d) DATA=("$OPTARG");;
    v) TEST_VERSION=$OPTARG;;
    o) OUT=$OPTARG;;
    n) N=$OPTARG;;
    s) SUBDIRS=("$OPTARG");;
    h) echo "Options: -d datasets (def: ${DATA[*]})";
       echo "         -v test version (def: ${TEST_VERSION})";
       echo "         -o output directory (def: ${OUT})";
       echo "         -s subdirectories (def: ${SUBDIRS[*]})";
       exit 0 ;;
  esac
done


# skip over the processed options
shift $((OPTIND-1))


echo $$ > "${PA}/norun_${HOST}.pid"


for f in ${DATA[*]}; do

    DIR=$PA/$OUT/$f/$TEST_VERSION/

    for SUBDIR in ${SUBDIRS[*]}; do
        mkdir -p $PA/$OUT/$f/$TEST_VERSION/$SUBDIR

        IT=$SUBDIR

        for i in {1..30}; do
            echo "Iteration ${i}"
            $PA/source/main.py -f $PA/maps/$f -a $ALPHA -d $DISCOUNT -n $N --stats "${DIR}${SUBDIR}/out_${f}" -e $EPSILON
        done
    done

done
