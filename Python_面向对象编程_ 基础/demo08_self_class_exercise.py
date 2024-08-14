# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午12:43
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
定义Person类
1.里面有name,age属性
2.并提供compare_to比较方法，用于判断是否和另一个人相等
3.姓名和年龄一样，就返回True,否则返回False
"""


class Person:
    name = None
    age = None

    def compare_to(self, other):
        # if self.name == other.name and self.age == other.age:
        #     return True
        # else:
        #     return False
        return self.name == other.name and self.age == other.age


f1 = Person()
f1.name = "小明"
f1.age = 18
f2 = Person()
f2.name = "小明"
f2.age = 19
print(f1.compare_to(f2))
