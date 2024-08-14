# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午9:59
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
1.编写一个Person类，包括属性(name, age),构造方法,say方法(返回Person自我介绍的字符串)
2.编写一个Student类，继承Person类，增加属性(id,score),以及构造方法，重写say方法(返回Student自我介绍的信息)
3.分别创建Person/Student对象，调用say方法输出自我介绍，体会重写的作用
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"我是{self.name},今年{self.age}"


class Student(Person):
    def __init__(self, name, age, id, score):
        super().__init__(name, age)
        self.id = id
        self.score = score

    def say(self):
        return f"{super().say()},id为{self.id},分数:{self.score}"


student = Student("A", 18, 1001, 60)
person = Person("A", 20)
print(student.say())
print(person.say())
