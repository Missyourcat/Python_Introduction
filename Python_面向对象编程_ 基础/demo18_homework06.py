# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i=", self.i)
        print("j=", j)


d1 = Demo()
d2 = d1
d2.m()
print(d1.i)
print(d2.i)
