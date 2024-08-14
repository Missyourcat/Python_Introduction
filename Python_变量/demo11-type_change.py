# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/13 下午10:15
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 隐式类型转换
# Python会根据该变量使用的上下文（即 当前值）在运行时决定的类型
var1 = 10
print(type(var1))  # int类型
var1 = 1.1
print(type(var1))  # float类型
var1 = "我爱Python"
print(type(var1))  # str类型

# 在运算的时候，数据类型会向高精度转化，float的精度高于int
var2 = 10
var3 = 1.2
var4 = var2 + var3
print("var4=", var4, "var4的类型: ", type(var4))
var2 = var2 + 0.1
print("var2=", var2, "var2的类型: ", type(var2))
