#!/bin/bash
NUM=12345
Ba=12233
BA=434987
HOSTNAME=$(hostname)
DAY=`date +%A`
1value=333
a=A
False@Var=False
Hyphen_a=WrongValue

echo "Variable NUM Value: $NUM"
echo "Variable Ba Vaule: $Ba"
echo "Variable BA Vaule: $BA"
echo "Variable HOST value: $HOSTNAME"
echo "Variable DAY value: $DAY"
echo "Wrong Variable 1value $1value" #number is not allowed
echo 'False @ Variable' $False@Var   # @ is not allowed
echo "hyphen-a Variable Value: $Hyphen_a" # _is allowed
echo "sall caps $a"
