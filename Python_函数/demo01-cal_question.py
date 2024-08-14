# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午10:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

n1 = float(input("请输入第一个数:"))
n2 = float(input("请输入第二个数:"))
operator = input("请输入运算符 +,-,*,/ :")
res = 0.0
if operator == "+":
    res = n1 + n2
elif operator == "-":
    res = n1 - n2
elif operator == "*":
    res = n1 * n2
elif operator == "/":
    res = n1 / n2
else:
    print("输入符号错误！")
print(f"{n1} {operator} {n2} = {res}")