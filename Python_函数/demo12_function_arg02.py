# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午9:54
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# f3接收多个函数作为参数传入
def f3(my_fun, num1, num2, my_fun2):
    return my_fun2(num1, num2), my_fun(num1, num2)


# 定义一个函数，可以返回两个数的最大值
def get_max_val(num1, num2):
    max_val = num1 if num1 > num2 else num2
    return max_val


# 定义函数返回两个数的和
def get_sum(num1, num2):
    return num1 + num2


print(f3(get_max_val, 130, 190, get_sum))
