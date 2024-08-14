# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午7:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from abc import *

"""
1.编写一个Employee类，做成抽象基类，包含如下三个属性：name,id,salary,提供必要的构造器和抽象方法work（）
2.对于Manage类来说，他即是员工，还有奖金（bouns）属性，请使用继承的思想，设计
CommonEmployee和Manage类，要求实现work（），提示“经理/普通员工 名字 工作中。。。”
"""


class Employee(ABC):
    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    @abstractmethod
    def work(self):
        pass

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id


class Manager(Employee):
    def __init__(self, name, id, salary, bonus):
        super().__init__(name, id, salary)
        self.__bonus = bonus

    def work(self):
        print(f"经理 {self.get_name()} 在工作。。。")


class CommonEmployee(Employee):
    def work(self):
        print(f"普通员工 {self.get_name()} 在工作。。。")


commonemployee = CommonEmployee("A", 1001, 1000)
manager = Manager("B", 100, 20000, 200)
manager.work()
commonemployee.work()
