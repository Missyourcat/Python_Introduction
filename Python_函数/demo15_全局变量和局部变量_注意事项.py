# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午10:13
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 1.未在函数内部重新定义n1,那么默认使用全局变量n1
n1 = 100


def f1():
    print(n1)


f1()

# 2.在函数内部重新定义了n1,那么根据就近原则，使用的就是函数内部重新定义的n1
n2 = 100


def f2():
    n2 = 200
    print(n2)


f2()
print(n2)

# 3.在函数内部使用global关键字，可以标明指定使用全局变量
n3 = 100


def f3():
    global n3
    n3 = 200
    print(n3)


f3()
print(n3)
