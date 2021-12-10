#!/bin/bash
a=$1
b=$2
c=$3
for (( i=0; i<$1; i++ ))
do
    echo -n "$2"
    fn=$(($2 + $3))
    a=$3
    b=$fn
done