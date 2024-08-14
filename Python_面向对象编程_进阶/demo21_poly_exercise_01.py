# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:47
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class A:
    i = 10

    # 当调用对象成员的时候，会和对象本身动态关联
    def sum(self):
        return self.getI() + 10

    def sum1(self):
        return self.i + 10

    def getI(self):
        return self.i


class B(A):
    i = 20

    # def sum(self):
    #     return self.getI() + 20
    #
    # def sum1(self):
    #     return self.i + 10

    def getI(self):
        return self.i


b = B()
print(b.sum())
print(b.sum1())
