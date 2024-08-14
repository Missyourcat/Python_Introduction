# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午7:36
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from abc import ABC, abstractmethod


# Animal是抽象类
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def cry(self):
        # print("不知道是什么动物")
        pass


# 编写子类Tiger继承Animal并实现抽象方法
class Tiger(Animal):
    def cry(self):
        print(f"老虎{self.name}嗷嗷叫")


# 抽象类（含有抽象方法），不能实例化
# animal = Animal(3)
tiger = Tiger("皮皮", 2)
tiger.cry()
