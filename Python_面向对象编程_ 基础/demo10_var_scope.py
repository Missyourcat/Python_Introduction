# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午12:59
# @Note     :   仅作学习使用--禁止传播，违者必究✅
class Cat:
    # 属 性
    name = None
    age = None

    # n1 n2 result 就是局部变量
    def cal(self, n1, n2):
        result = n1 + n2
        print(f"result:{result}")
        print(f"cal()使用属性name{self.name}")

    def cry(self):
        print(f"cry()使用属性name{self.name}")

    def eat(self):
        print(f"eat()使用属性name{self.name}")


cat = Cat()
cat.cal(10, 20)
cat.cry()
cat.eat()


class Dog:
    # 属性
    name = None
    age = None

    def hi(self):
        name = '皮皮'
        print(f"name = {name}")
        print(f"name = {self.name}")


dog = Dog()
dog.hi()
dog.name = "小米"
dog.hi()
