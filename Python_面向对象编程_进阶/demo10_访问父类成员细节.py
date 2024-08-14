# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午9:31
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 子类不能直接访问父类的私有成员
class A:
    n1 = 100
    __n2 = 600

    def run(self):
        print("A-run()")

    def __jump(self):
        print("A-jump()")


class B(A):
    def say(self):
        print("say()")
        # 子类不能直接访问父类的私有成员
        # print(A.__n2)
        # print(super().__n2)
        # A.__jump(self)
        # super().__jump()


b = B()
b.say()


# 访问不限于直接父类，而是建立从子类向上级父类的查找关系 A->B->C
class Base:
    n3 = 800

    def fly(self):
        print("Base-fly()")


class A(Base):
    n1 = 100
    __n2 = 200

    def run(self):
        print("A-run()")

    def __jump(self):
        print("A-jump()")


class B(A):
    def say(self):
        print("say()..")
        """
        Base.n3: 表示直接访问Base类的n3属性
        A.n3: 表示直接访问A类的n3
        super().n3: 表示从B类的直接父类A类去访问n3
        """
        print(Base.n3, A.n3, super().n3)
        """
        Base.fly(self): 表示直接访问Base的fly方法
        A.fly(self): 表示直接访问A类的fly方法
        super().fly(): 表示访问直接父类A的fly方法
        self.fly(): 表示访问本类的fly方法
        """
        Base.fly(self)
        A.fly(self)
        super().fly()
        self.fly()


b = B()
b.say()

# 建议使用super()的方式,如果使用 父类名 方式，一旦父类变化，类名统一需要修改，比较麻烦
