#!/bin/bash

for (( i=0; i<$1; i++ ))
do
    echo -n "$2"
    fn=$(($2 + $3))
    a=$3
    b=$fn
done