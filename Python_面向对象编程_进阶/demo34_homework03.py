# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午10:26
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
编写Doctor类，属性：name,age,job,gender,sal 5个参数的构造器
重写__eq__()方法，并判断测试类中创建的两个对象是否相等
"""


class Doctor:
    def __init__(self, name, age, job, gender, sal):
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender
        self.sal = sal

    def __eq__(self, other):
        if not isinstance(other, Doctor):
            return False
        else:
            return self.name == other.name and \
                self.sal == other.sal and \
                self.job == other.job and \
                self.gender == other.gender and \
                self.age == other.age


doctor1 = Doctor("kong", 20, "医生", "男", 100)
doctor2 = Doctor("kong", 20, "医生", "男", 100)
print(doctor1 == doctor2)
