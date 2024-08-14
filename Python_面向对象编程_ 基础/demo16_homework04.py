# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 编程创建一个Cal计算类，在其中定义2个成员变量表示操作数，定义四个方法实现求和，差，乘，商(要求除数为0的话，要提示)并创建对象，分别测试
class Cal:
    num1 = None
    num2 = None

    def __init__(self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def get_sum(self):
        return self.num1 + self.num2

    def get_minus(self):
        return self.num1 - self.num2

    def get_mul(self):
        return self.num1 * self.num2

    def get_div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "除数不能为0"


a = Cal(3, 0)
print(a.get_sum())
print(a.get_minus())
print(a.get_mul())
print(a.get_div())
