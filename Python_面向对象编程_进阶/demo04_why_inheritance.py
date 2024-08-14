# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午9:39
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Pupil:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score

    def testing(self):
        print("小学生在考小学数学。。。")


class Graduate:
    name = None
    age = None
    __score = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

    def set_score(self, score):
        self.__score = score

    def testing(self):
        print("大学生在考高等数学。。。")


pupil = Pupil('ok', 8)
graduate = Graduate('no', 22)
pupil.testing()
pupil.set_score(60)
pupil.show_info()
print("-" * 30)
graduate.testing()
graduate.set_score(60)
graduate.show_info()

"""
1.Pupil 和 Graduate 有很多相同的方法和属性
2.代码复用性差
3.不利于代码的维护和管理
"""
