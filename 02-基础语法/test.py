# 变量
heigth = 100


# 输入input
str_input = input("请输入内容:")


# 打印输入
print("输入的内容：%s" % str_input)


# 判断语
if int(heigth) > 99:
    print("判断heigth>99")
else:
    print("判断heigth<99")


# 类型转换
s = str(10)
i = int("11")
# l = long("223344");


# 运算符 //-取除  **-幂  *-乘
print("=" * 10)


# 输出多个变量
p_1 = 1231
p_2 = 'str'
p_3 = 'strs'
print("变量1：%d,变量2：%s,变量3：%s" % (p_1, p_2, p_3))

# 判断符
t_1 = True;
t_2 = False;
if t_1 or t_2:
    print("or执行条件");
if t_2 and t_2:
    print("and执行条件");
if not(t_2 and t_2):
    print("not执行条件");
