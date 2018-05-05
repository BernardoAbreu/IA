#!/bin/bash


INPUT_FILE=$1

while IFS=' ', read -r IX IY FX FY
do
    echo "I got:$IX|$IY|$FX|$FY"
done < $INPUT_FILE