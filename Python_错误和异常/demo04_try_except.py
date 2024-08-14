# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午7:14
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
try:
    可能出现异常的代码
except [异常 as 别名]
    发生异常时，对异常处理的代码
"""
try:
    num1 = 10
    num2 = 0
    res = num1 / num2

    # # 处理方式1
    # except:
    #     print("出现异常了")

    #     # 方式2 获取到异常
    #     """
    #     1.表示要捕获Exception 和它的子类类型异常
    #     2.捕获的范围 是比较大的
    #     """
    # except Exception as e:
    #     print(f"捕获到异常，异常的信息是{e},类型是{type(e)}")

# 方式3 捕获具体的异常
except ZeroDivisionError as e:
    print(f"捕获到异常ZeroDivisionError")

print("程序继续执行")
