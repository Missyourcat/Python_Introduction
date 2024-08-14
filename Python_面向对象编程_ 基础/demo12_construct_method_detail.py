# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:30
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 一个类只有一个__init__方法,即使你写了多个，最后也只有一个生效
# class Person:
#     name = None
#     age = None
#
#     def __init__(self, name, age):
#         print(f"__init__执行了...得到{name} {age}")
#         self.name = name
#         self.age = age
#
#     def __init__(self, name):
#         print(f"__init__执行了...得到{name}")
#         self.name = name
#
#
# # p1 = Person("kobe", 20) # 报错
# p1 = Person("kobe")
# print(f"p1的name = {p1.name} age = {p1.age}")

# python可以动态的生成对象属性
class Person:
    def __init__(self, name, age):
        print(f"__init__执行了...得到{name} {age}")
        self.name = name
        self.age = age


p1 = Person('tim', 30)
print(f"p1的name = {p1.name} age = {p1.age}")

# 构造方法不能有返回值
# class Person:
#     def __init__(self, name, age):
#         print(f"__init__执行了...得到{name} {age}")
#         self.name = name
#         self.age = age
#         # return 1
#
# p1 = Person('tim', 30)
# print(f"p1的name = {p1.name} age = {p1.age}")
