# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:43
# @Note     :   仅作学习使用--禁止传播，违者必究✅

try:
    # num1 = 10
    # num2 = 0
    # res = num1 / num2
    """
    raise用于主动的触发异常
    ZeroDivisionError：程序员指定的异常，可以根据需要指定
    """
    raise ZeroDivisionError("主动触发ZeroDivisionError")
except ZeroDivisionError as err:
    print(f"{err} {type(err)}")
