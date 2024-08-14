# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午9:14
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class A:
    n1 = 100

    def run(self):
        print("A-run()...")


class B(A):
    n1 = 200

    def run(self):
        print(f"8-run()...")

    # 通过父类名 去访问父类的成员
    def say(self):
        print(f"父类的n1: {A.n1} 本类的n1: {self.n1}")  # 子类没有n1去父类找
        # 调用父类的run
        A.run(self)
        # 调用本类的run
        self.run()

    # 通过super() 访问父类
    def hi(self):
        print(f"父类的n1 {super().n1}")
        super().run()


b = B()
b.say()
b.hi()
