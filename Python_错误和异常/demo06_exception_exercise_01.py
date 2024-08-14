# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:37
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 如果用户输入的不是一个整数，就提示他反复输入，知道输入一个整数为止
while True:
    try:
        a = int(input("请输入:"))
        break
    except Exception as e:
        print("输入有误")
print(a)