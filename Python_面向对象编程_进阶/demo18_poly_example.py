# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:26
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Animal:
    def cry(self):
        pass


class Cat(Animal):
    def cry(self):
        print("小猫 喵喵叫")


class Dog(Animal):
    def cry(self):
        print("小狗 汪汪叫")


class Pig(Animal):
    def cry(self):
        print("小猪 哼哼叫")


class AA:
    def cry(self):
        pass


# 在python 面向对象编程中，子类对象可以传递给父类类型
def fun(animal: Animal):
    print(type(animal))
    animal.cry()


cat = Cat()
dog = Dog()
pig = Pig()
fun(cat)


class AA:
    def hi(self):
        print("hi  AA")


class BB:
    def hi(self):
        print("hi  BB")


def test(obj):
    obj.hi()


aa = AA()
bb = BB()
test(aa)
test(bb)
