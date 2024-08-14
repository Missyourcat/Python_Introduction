# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午12:52
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Person:
    name = None
    age = None

    # 成员方法
    def hi(self):
        print("hi,python")

    def cal01(self):
        result = 0
        for i in range(1, 1001):
            result += i
        print(result)

    def cal02(self, n):
        result = 0
        for i in range(1, n + 1):
            result += i
        print(result)

    def get_sum(self, n1, n2):
        return n1 + n2


p = Person()
p.hi()
p.cal01()
p.cal02(10)
print(p.get_sum(10, 20))
