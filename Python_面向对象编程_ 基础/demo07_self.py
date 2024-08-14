# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午1:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# class Dog:
#     name = "波斯猫"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息:{name}")
#         print(f"属性name:{self.name}")
#
#
# dog = Dog()
# dog.info("加菲猫")

# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def info(self, name):
#         print(f"name信息:{name}")
#
#     # 静态方法
#     @staticmethod  # 通过@staticmethod可以将方法转为静态方法
#     def ok():  # 静态方法可以不带self ， 调用形式有变化
#         print("ok()...")
#
#
# dog = Dog()
# dog.info("德牧")
# # 调用静态
# # 通过对象调用
# dog.ok()
# # 通过类名调用
# Dog.ok()

# self表示当前对象本身，简单的说，那个对象调用，self就代表那个对象
# class Dog:
#     name = "藏獒"
#     age = 2
#
#     def hi(self):
#         print(f"hi self: {id(self)}")
#
#
# # self表示当前对象本身
# dog2 = Dog()
# print(f"dog2: {id(dog2)}")
# dog2.hi()
# print("-" * 30)
# dog3 = Dog()
# print(f"dog3: {id(dog3)}")
# dog3.hi()

# 通过对象调用时,self会隐式传入

# 方法内部，要访问成员变量和成员方法，需要使用self
class Dog:
    name = "藏獒"
    age = 2

    def eat(self):
        print(f"{self.name}饿了")

    def cry(self, name):
        print(f"{name} is crying")
        print(f"{self.name} is crying")
        self.eat()
        # 不能直接调用
        # eat()


dog = Dog()
dog.name = "中华田园犬"
dog.cry("金毛")
