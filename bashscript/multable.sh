clear
  echo "which number to generate multiplication table"
  read number
  i=1
  while [ $n -le 10 ]
  do
  echo " $number * $n =`expr $number \* $n ` "
  n=`expr $n + 1`
  done
