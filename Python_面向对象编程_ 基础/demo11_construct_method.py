# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 在初始化对象时，会自动执行__init__方法
# class Person:
#     # 构造方法/构造器
#     def __init__(self):
#         print("__init__执行了")
#
#
# p1 = Person()
# p2 = Person()

# 将传入的参数，自动传递给__init__方法
class Person:
    name = None
    age = None

    # 构造方法/构造器
    # 构造方法是完成对象的初始化任务
    def __init__(self, name, age):
        print(f"__init__执行了 {name} {age}")
        # 把接收到的name和age赋给属性
        # self就是你当前创建的对象
        print(f"self id:{id(self)}")
        self.name = name
        self.age = age


p1 = Person("kobe", 20)
print(f"p1 id:{id(p1)}")
p2 = Person("tim", 20)
print(f"p2 id:{id(p2)}")

# 构造方法是py预定义的，名称是__init__
