# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午7:43
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from abc import *


# 抽象类不能被实例化
# 抽象类需要继承ABC,并且需要至少一个抽象方法
# class AAA(ABC):
#     name = "time"
#
#     @abstractmethod
#     def f1(self):
#         pass
#

# obj = AAA()

# 抽象类可以有普通方法
# class AAA(ABC):
#     name = "time"
#
#     @abstractmethod
#     def f1(self):
#         pass
#
#     def hi(self):
#         print("hi")
#
#     def ok(self):
#         pass
#
#
# class BBB(AAA):
#     def f1(self):
#         print("BBB-f1")
#
#
# obj2 = BBB()
# obj2.f1()
# obj2.hi()
# obj2.ok()

# 如果一个类继承了抽象类，泽塔必须实现抽象类的所有抽象方法，否则它仍然是一个抽象类
class AAA(ABC):
    name = "time"

    @abstractmethod
    def f1(self):
        pass

    @abstractmethod
    def f2(self):
        pass

    def hi(self):
        print("hi")

    def ok(self):
        pass


class BBB(AAA):
    def f1(self):
        print("BBB-f1")

    def f2(self):
        print("BBB-f2")


obj2 = BBB()
obj2.f1()
obj2.f2()
obj2.hi()
obj2.ok()
