# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午4:35
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 没有重写__eq__前，比较的内存地址
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and \
                self.age == other.age and \
                self.gender == other.gender
        else:
            return False

    # self < other 重写
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.age < other.age
        else:
            return "类型不一致不能比较"

    # self <= other 重写
    def __le__(self, other):
        if isinstance(other, Person):
            return self.age <= other.age
        else:
            return "类型不一致不能比较"

    # self ！= other
    def __ne__(self, other):
        return not self.__eq__(other)


class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


p1 = Person("smith", 20, '男')
p2 = Person("smith", 20, '男')
p3 = Dog("smith", 20, '男')
print(f"p1==p2:{p1 == p2}")
print(f"p1==p3:{p1 == p3}")
print(f"p1 < p2:{p1 < p2}")
print(f"p1 < p2:{p1 <= p2}")
print(f"p1!=p2:{p1 != p2}")
