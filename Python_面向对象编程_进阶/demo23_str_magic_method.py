# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午4:27
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Monster:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        # 根据需要重写__str__
        """
        默认情况调用的是父类object的__str__
        父类object的__str__返回的就是类型+地址
        可以根据需要重写
        :return:
        """
        # return super().__str__()
        return f"{self.name} {self.age} {self.gender}"


m = Monster("青牛怪", 500, "男")
print(m)  # <__main__.Monster object at 0x79eead9f14f0>
