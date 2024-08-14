# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:51
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# def f3():
#     print("f3 start")
#     try:
#         print(10 / 0)
#     except Exception as e:
#         print(f"f3捕获异常 {e}")
#     print("f3 end")
#
#
# def f2():
#     print("f2 start")
#     f3()
#     print("f2 end")
#
#
# def f1():
#     try:
#         f2()
#     except Exception as e:
#         print(f"f1捕获异常 {e}")
#
#
# f1()
# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:51
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# def f3():
#     print("f3 start")
#     print(10 / 0)
#     print("f3 end")
#
#
# def f2():
#     print("f2 start")
#     try:
#         f3()
#     except Exception as e:
#         print(f"f2捕获异常 {e}")
#     print("f2 end")
#
#
# def f1():
#     try:
#         f2()
#     except Exception as e:
#         print(f"f1捕获异常 {e}")
#
#
# f1()

def f3():
    print('f3 start')
    print(10 / 0)
    print('f3 end')


def f2():
    print('f2 start')
    f3()
    print('f2 end')


def f1():
    f2()


f1()
