#!/bin/bash
<<com

# if else and elif syntax goes here














# class task 


# 1 greatest of 3 number using if statement

echo "enter 1st number "
read A
echo " enter 2nd number"
read B
echo " enter 3rd number"
read C

if [ $A -gt $B -a $A -gt $C ]
then
echo " $A is greatest"
elif [ $B -gt $C ]
then
echo "$B is greatest"
else
echo " $C is greatest"
fi



# 2 even or odd

echo "enter a number"
read A
if [ $(($A%2)) -eq 0 ];then
echo " $A is even "
else
echo "$A is odd "
fi






# case  syntax goes here














# task 

#1 find grade using case


echo " enter the marks "
read M

case $(($M/10)) in
10) echo " grade A";;
9) echo "grade A";;
8) echo " grade B";;
7) echo " grade C";;
6) echo " grade C";;
5) echo " grade D";;
4)echo " grade D";;
3)echo " grade F";;
2)echo " grade F";;
1)echo " grade F";;
0)echo "grade F";;
*)echo " enter only between 0-100 "
esac
com
