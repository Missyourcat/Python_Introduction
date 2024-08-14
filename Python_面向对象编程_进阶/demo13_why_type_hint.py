# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午10:10
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
1.类型提示，防止运行时出现参数类型，返回值类型，变量类型不符合
2.作为开发文档附加说明，方便使用这个和调用时传入和返回参数类型
3.加入后并不会影响程序的运行，不会报正式的错误，只是提醒
4.PyCharm 支持类型注解，参数类型错误会黄色提示
"""


# a: str:给形参a进行类型注解，标注a的类型是str
def fun1(a: str):
    for i in a:
        print(i)


fun1(1)
fun1("100")
