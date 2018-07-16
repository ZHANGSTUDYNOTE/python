#!bin/bash
my_name="zhang..."
echo $my_name

#只读变量,只读变量不能删除
my_url="http://www.runoob.com/linux/linux-shell-variable.html" readonly my_url
echo $my_url

#获取字符串长度
echo $my_url |wc -L #提取字符串

#提取字符串
echo ${my_url:0:5}

#数组
my_array=(a b c 1 2 3)
echo ${my_array}

#数组长度
echo ${#my_array[@]}
echo ${#my_array[*]}
echo ${#my_array[n]}

#删除变量
unset my_name

:<< EOF
多行注释。。。
多行注释。。。
EOF
