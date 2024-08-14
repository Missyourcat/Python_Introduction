# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
当我们接受Person年龄时，要求范围在18-200之间，否则抛出一个自定义异常
并给出提示
"""


class AgeError(Exception):
    pass


while True:
    try:
        age = int(input("亲输入年龄:"))
        if not (18 <= age <= 120):
            raise AgeError("年龄需要在18-120之间")
        break
    except ValueError as e:
        print("你输入的不是整数")
    except AgeError as e:
        print(e)
