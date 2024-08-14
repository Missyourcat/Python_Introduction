# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午7:28
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
创建职员类(Clerk),属性有name,job,salary
1.不能随便查看职员Clerk的职位和工资等隐私
2.提供公共方法，可以对职位和工资进行操作
"""


class Clerk:
    # 公共属性
    name = None
    # 私有属性
    __job = None
    __salary = None

    # 构造方法
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    # 提供公共方法，对私有属性进行操作
    def set_job(self, job):
        self.__job = job

    def get_job(self):
        return self.__job

    # 私有方法
    def __hi(self):
        print("hi")

    # 提供公共方法，操作私有方法
    def f1(self):
        self.__hi()


clerk = Clerk("tiger", "python工程师", 20000)
# 如果是公共属性，在类的外部可以直接访问
print(clerk.name)
# 如果是私有属性，在类的外部不可以直接访问
# print(clerk.__job)
print(clerk.get_job())
clerk.set_job("java工程师")
print(clerk.get_job())
# 通过公共方法调用私有方法
clerk.f1()
