# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午4:51
# @Note     :   仅作学习使用--禁止传播，违者必究✅
class Monster:
    name = "蝎子精"
    age = 300

    def hi(self):
        print(f"hi() {self.name}-{self.age}")


print(Monster)
# 通风class对象，可以引用属性（没有创建实例对象也可以引用/访问）
print(f"Monster.name: {Monster.name} Monster.age: {Monster.age}")
# 通过类名如何调用非静态成员方法
Monster.hi(Monster)
