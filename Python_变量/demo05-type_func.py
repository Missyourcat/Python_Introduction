# @System   :   Arch Linux
# @Author   :   MR.申
# @File     :   demo02-快捷键|转义字符.py
# @Time     :   2024/7/6 下午3:06
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 演示type()使用
name = "tom"  # 字符串
age = 20  # 整形
score = 99.9  # 浮点型(小数)
gender = "男"  # 字符串
is_pass = True  # bool类型

print(type(name))
print(type(age))
print(type(score))
print(type(gender))
print(type(is_pass))

name = 100
print(type(name))

# type可以直接查看具体的值(字面量)的类型
print(f"hello的类型是{type('hello.txt')}")
print(f"hello的类型是{type("hello.txt")}")
print(f"1.1的类型是{type(1.1)}")
print(f"30的类型是{type(30)}")
print(f"True的类型是{type(True)}")
print(f"False的类型是{type(False)}")
