# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午12:23
# @Note     :   仅作学习使用--禁止传播，违者必究✅
class Person:
    age = None
    name = None


p1 = Person()
p1.age = 10
p1.name = "小明"
p2 = p1
print(p2.age)
print(f"p1.name地址:{id(p1.name)} p2.name地址:{id(p2.name)}")

a = Person()
a.age = 10
a.name = 'jack'
b = a
print(b.name)
b.age = 200
b = None
print(a.age)
# print(b.age)
