# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午10:05
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
子类继承了所有的属性和方法，菲斯有的属性和方法可以在子类直接访问
但是私有属性和方法不能在子类直接访问，要通过父类提供公共的方法去访问
"""


class Base:
    n1 = 100
    __n2 = 200

    def __init__(self):
        print("Base 构造方法...")

    def hi(self):
        print("hi() 公共方法")

    def __hello(self):
        print("__hello 私有方法")

    # 提供公共方法，返回私有的属性和方法
    def test(self):
        print("属性: ", self.n1, self.__n2)
        self.__hello()


class Sub(Base):
    # 子类的构造器
    def __init__(self):
        print("sub 构造方法")

    def say_ok(self):
        print("say_ok()", self.n1)
        self.hi()
        # print(self.__n2)
        # self.__hello()


sub = Sub()
sub.say_ok()

# 调用子类继承父类的公共方法，趋势线访问父类的私有方法
sub.test()


# Ctrl + H 查看继承关系
# Python编程语言中,object是所有其他类的基类

# python 支持多重继承
class A:
    n1 = 100

    def sing(self):
        print("A sing()", self.n1)


class B:
    n2 = 200
    n1 = 120

    def dance(self):
        print("B dance()", self.n2)


class C(A, B):
    pass


c = C()
print("-" * 30)
print(f"属性信息{c.n1} {c.n2}")
c.dance()
c.sing()

# 在多重继承中，如果同名的成员，遵循从左到右的继承优先级(即:写左边的父类优先级高，写在右边的父类优先级低)
