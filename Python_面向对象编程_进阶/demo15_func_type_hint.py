# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:01
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
1.name: str  对形参name进行类型注解：标注name类型是str
2.在调用方法/函数时，传入的实参类型不是一样的，则给出警告
"""


def fun1(name: str):
    for ele in name:
        print(ele)


fun1("python")

"""
1.a: int, b: int 对形参a,和b进行类型注解，标注a,b的类型为int
2.-》int 对返回值进行类型注解，标注返回值类型为int
类型注解是提示性的，并不是强制性
"""


def fun2(a: int, b: int) -> int:
    return a + b


print(f"结果是:{fun2(10, 20)}")
