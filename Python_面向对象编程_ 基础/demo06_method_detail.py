# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午12:59
# @Note     :   仅作学习使用--禁止传播，违者必究✅

def hi():
    print("hi python")


class Person:
    name = None
    age = None

    def ok(self):
        pass


p = Person()
p2 = Person()
"""
1.动态的给p对象添加方法m1,注意只是针对p对象添加方法
2.m1是你新增加的方法的名称，由程序员指定名字
3.即m1方法和函数hi关联起来
"""
p.m1 = hi
p.m1()
print(type(p.m1), type(hi))
print(type(p.ok))
