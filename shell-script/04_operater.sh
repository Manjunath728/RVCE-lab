#!/bin/bash


echo -e "enter first number"
read -r a
echo -e "enter second number"
read -r b


#arthmetic operater

echo "a+b is $(($a+$b))"
echo "a-b is `expr $a - $b`"
echo "a*b is $(($a*$b))"
echo "a/b is $(($a/$b))"
echo "a%b is $(($a%$b))"


#logical operater 

echo " 0 is false and 1 is true "
echo "a > b : $(($a>$b)) "
echo "a < b : $(($a<$b)) "
echo "a == b : $(($a==$b)) "
echo "a != b : $(($a!=$b)) "

