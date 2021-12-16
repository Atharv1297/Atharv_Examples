clear
  i=1
  while [ "$n" != 10 ]
  do
  echo " $1 * $n =`expr $1 \* $n ` "
  n=`expr $n + 1`
  done
