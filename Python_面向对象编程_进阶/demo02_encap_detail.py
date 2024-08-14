# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午9:16
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Clerk:
    def __init__(self, name, job, salary):
        self.name = name
        self.__salary = salary
        self.__job = job

    def get_job(self):
        return self.__job


clerk = Clerk("apple", "python工程师", 20000)
"""
如果这样使用，因为python的动态特性，会动态的创建属性__job
但是这个属性，和我们在类中定义的属性__job并不是同一个变量，我们在类中定义的__job 私有属性完整的名字是_Clerk__job
"""
clerk.__job = "go工程师"
print(clerk.__job)
print("ok")
print(clerk.get_job())
