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


#relatinal operater

echo " 0 is true and 1 is false "
test $a -gt $b ; echo " a is greater than b : $?"
test $a -ge $b ; echo " a is greater than or equal to b : $?"
test $a -lt $b ; echo " a is less than b : $?"
test $a -le $b ; echo " a is less than or equal to b : $?"
test $a -eq $b ; echo " a equal to b : $?"
test $a -ne $b ; echo " a not eaqual to b : $?"


# logical operrater

# -a is used as logical AND
# -o is uded as logical OR
# 
