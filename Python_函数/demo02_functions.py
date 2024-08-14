# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 上午12:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 1.自定义cry函数，输出"小猫，喵喵叫。。"
# 定义函数
def cry():
    print("小猫，喵喵叫。。。")


# 调用函数
cry()


# 2.自定义cal01函数，可以计算从1+。。。+1000的结果
def cal01():
    total = 0
    for i in range(1, 1001):
        total += i
    print("total =", total)


cal01()


# 3.自定义cal02函数，该函数可以接收一个数n,计算1+...+n的结果
def cal02(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print("total =", total)


cal02(10)


# 4.自定义get_sum函数，可以计算两个数的和，并返回结果
def get_sum(num1, num2):
    return num1 + num2


print(get_sum(1, 2))


# 5.使用函数来解决前面的计算题
def cal04():
    n1 = float(input("请输入第一个数:"))
    n2 = float(input("请输入第二个数:"))
    operator = input("请输入运算符 +,-,*,/,// :")
    res = 0.0
    if operator == "+":
        res = n1 + n2
    elif operator == "-":
        res = n1 - n2
    elif operator == "*":
        res = n1 * n2
    elif operator == "/":
        res = n1 / n2
    elif operator == "//":
        res = n1 // n2
    else:
        print("输入符号错误！")
    print(f"{n1} {operator} {n2} = {res}")


cal04()
