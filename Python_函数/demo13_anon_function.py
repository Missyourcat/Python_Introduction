# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午10:00
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 编写一耳光函数，可以接收一个匿名函数和两个数，通过匿名函数计算，返回两个数的最大值
def f1(fun, num1, num2):
    """
    功能:调用fun返回num1和num2的最大值
    :param fun: 接收函数（匿名）
    :param num1:
    :param num2:
    :return:
    """
    print(f"fun类型:{type(fun)}")
    return fun(num1, num2)


# 关键看如何调用匿名函数
"""
    1. lambda a, b: a if a > b else b 匿名函数
    2. 不需要return,运算结果就是返回值
"""
max_val = f1(lambda a, b: a if a > b else b, 1, 2)
print("max_val=", max_val)
