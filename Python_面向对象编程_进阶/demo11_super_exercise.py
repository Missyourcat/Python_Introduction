# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午9:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A-fly()")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B-fly()")


class C(B):
    n1 = 100

    def fly(self):
        print("C-fly()")

    def say(self):
        print(self.n1)
        print(self.n2)
        print(self.n3)
        print(super().n1)
        print(B.n1)
        print(C.n1)
        self.fly()
        A.fly(self)


c = C()
c.say()
