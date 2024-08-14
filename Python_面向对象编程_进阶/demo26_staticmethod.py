# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午4:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f"hi() {self.name}-{self.age}")

    @staticmethod
    def ok():
        print("ok")


# 不需要实例化，通过类即可调用静态方法
Monster.ok()
# 通过实例对象，也可以调用静态方法
monster = Monster()
monster.ok()
Monster().ok()
