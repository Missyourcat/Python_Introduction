# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 上午3:47
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 捕获异常，进行处理，这样程序可以在出现异常的情况下，继续执行
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except Exception as e:
    print("捕获到异常了，异常是", e)
print("继续运行。。。")
