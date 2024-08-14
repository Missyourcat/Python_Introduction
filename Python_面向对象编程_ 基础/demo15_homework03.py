# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from math import pi


# 定义一个圆类Circle,定义属性:半径，提供显示圆周长功能的方法，提供显示圆面积的方法
class Circle:
    radius = None

    def __init__(self, radius):
        self.radius = radius

    def c_round(self):
        c_round = self.radius * 2 * pi
        print("周长为", round(c_round, 2))

    def area(self):
        area = self.radius ** 2 * pi
        print("面积为", area)


C1 = Circle(5)
C1.c_round()
C1.area()
