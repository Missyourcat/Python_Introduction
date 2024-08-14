# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午5:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅

def test(n):
    if n > 2:
        test(n - 1)
    print("n=", n)


test(4)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(4))
