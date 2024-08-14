# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:48
# @Note     :   仅作学习使用--禁止传播，违者必究✅
def f3():
    print("f3 start")
    print(10 / 0)
    print("f3 end")


def f2():
    print("f2 start")
    f3()
    print("f2 end")


def f1():
    try:
        f2()
    except Exception as e:
        print(f"f1捕获异常 {e}")


f1()
