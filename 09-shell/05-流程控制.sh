#!/bin/bash

#for循环
for loop in 1 2 3 4 5 
do
   echo $loop
done


#while循环
echo "====================================="
int=1
while(( $int<=5 ))
do
    echo $int
    let "int++"
done


#until循环
echo "====================================="
a=0
until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done


#Shell case语句为多选择语句。
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac


#break跳出循环
