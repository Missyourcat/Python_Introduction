# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 上午12:32
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 函数的命名遵循标识符命名规则和规范
# def 2f():  # 不能以数字开头
#     print("2f")
# def a-b():  # 非法字符
#     print("a-b")

# 函数中的变量是局部的，函数外不生效
def hi():
    n = 10
    print("n =", n)


hi()


# print("n =", n)

# 如果同一个文件，出现两个函数名相同的函数，则以就近原则进行调用
def cry(n):
    print("cry()..hi..", n)


cry(5)


def cry():
    print("cry()..ok..")


# 默认接近第二个cry()
cry()


# 调用函数时，根据函数定义的参数位置来传递参数，这种传参方法就是位置参数，传递的实参和定义的形参顺序和个数必须一致，同时定义的形参，不用指定数据类型，会根据传入的实参决定
def car_info(name, price, color):
    print(f"name->{name} price->{price} color->{color}")


car_info("jack", 100, "red")


# car_info("jack", 100, "red", 11)


# 函数可以有多个返回值
def f2(n1, n2):
    return n1 + n2, n1 - n2


r1, r2 = f2(1, 2)
print(f"r1->{r1} r2->{r2}")


# 函数支持关键字参数
# 函数调用时，可以通过“形参名=实参值”形式传递参数，这样可以不受参数传递顺序的限制
def book_info(name, price, author, amount):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


book_info("红楼梦", 30, "曹雪芹", 30000)
book_info("红楼梦", 30, 3000, "曹雪芹")
print("--------------关键字-----------------")
book_info(name="红楼梦", price=30, amount=30000, author="曹雪芹")
book_info("红楼梦", 30, amount=30000, author="曹雪芹")


# 函数支持默认参数/缺省参数
# 定义函数时，可以给参数提供默认值，调用函数时，指定了实参，则以指定为准，没有指定，则以默认值为准
# 默认参数，需要放在参数列表后
def book_info2(name='<<thinking is python>>', price=66.8, author='龟叔', amount=100):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


book_info2()
book_info2('<<study python>>')


# def book_info3(author='鬼鼠', amount=100, name, price):
def book_info3(name, price, author='鬼鼠', amount=100):
    print(f"name->{name} price->{price} author->{author} amount->{amount}")


book_info3("<<python揭秘>>", 999)

# 函数支持可变参数/不定长参数
"""
应用场景：当调用函数时，不确定传入多少个实参的情况
传入的多个实参，会被组成一个元组(tuple),元组可以存储多个数据项
"""


# 要计算多个数的和，但是不确定是几个数 *[0到多]
def sum(*args):  # args->(1, 2, 3, 100)0
    print(f"args->{args} 类型是->{type(args)}")
    total = 0
    for ele in args:
        total += ele
    return total


result = sum(1, 2, 3, 100)
print(f"result->{result}")
result = sum()
print(f"result->{result}")

# 函数的可变参数/不定长参数 还支持多个关键字参数，也就是 多个“形参名=实参值”
"""
应用场景:当调用函数时，不确定传入多少个 关键字的情况
传入多个关键字参数，会被组成一个字典(dict),字典可以存储=多个 键=值 的数据项
"""


def person_info(**args):  # 关键字可变参数
    print(f"args->{args} 类型->{type(args)}")
    for arg_name in args:
        print(f"参数名->{arg_name} 参数值->{args[arg_name]}")


person_info(name="sh", age=18, email="1781196585@qq.com")
person_info(name="sh", age=18, email="1781196585@qq.com", sex="男")
person_info()

# Python可以调用另一个.py文件中的函数
import demo02_functions  # 应该做代码最上方

demo02_functions.get_sum(1, 2)
