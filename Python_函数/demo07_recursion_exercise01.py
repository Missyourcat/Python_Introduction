# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午5:37
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 请使用递归的方式求出斐波那契数1,1,2,3,5,8,13...给你一个整数n,求出它的值是多少
def fbn(n):
    """
    功能:返回n对应的斐波那契数
    :param n: 接受一个整数n》=1
    :return: 返回斐波那契数
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fbn(n - 1) + fbn(n - 2)


print(fbn(40))

