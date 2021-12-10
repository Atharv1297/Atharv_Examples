echo "enter the limit for series"
N=6

echo "enter the First number for series"
a=0
  
echo "enter the Second number for series"
b=1 
   
echo "The Fibonacci series is : "
   
for (( i=0; i<N; i++ ))
do
    echo -n "$a "
    fn=$((a + b))
    a=$b
    b=$fn
done