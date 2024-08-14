# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午10:00
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 定义一个Person类，属性name,age.job,创建Person列表，有3个person对象，并按照age从大到小进行排序
class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def __str__(self):
        return f'{self.name} {self.age} {self.job}'


p1 = Person('A', 20, "java")
p2 = Person('A2', 22, "python")
p3 = Person('A1', 25, "c")
my_list = [p1, p2, p3]
for p in my_list:
    print(p)


def BubbleSort(my_list: list[Person]):
    for i in range(len(my_list)):
        for j in range(len(my_list) - i - 1):
            if my_list[j].age < my_list[j + 1].age:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


print("-" * 30)
# BubbleSort(my_list)
"""
 sort 解决
 key=lambda ele: ele.age表示我指定安装列表元素的age属性进行排序
 reverse=True 表示逆序
"""
my_list.sort(key=lambda ele: ele.age, reverse=True)
for p in my_list:
    print(p)
