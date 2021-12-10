#!/bin/bash
a=$a
b=$3
for (( i=0; i<$1; i++ ))
do
    echo -n "$a"
    fn=$(($a + $b))
    a=$b
    b=$fn
done