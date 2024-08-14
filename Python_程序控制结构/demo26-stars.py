    # @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午5:51
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 编写一个程序，可以接收一个整数，表示层数total_level,打印空心金字塔
"""
思路分析：
-先死后活
1.先不考虑层数的变化，假定就是5层，后面做活
-化繁为简
1.打印矩阵
2.打印直角三角形
3.打印金字塔
4.打印空心金字塔
"""
total_level = 5
for i in range(1, total_level + 1):
    for j in range(1, total_level + 1):
        print("*", end="")  # end=""表示不换行
    print("")
print("-------------------------")
for i in range(1, total_level + 1):
    for j in range(i):
        print("*", end="")  # end=""表示不换行
    print("")
print("--------------------------")
for i in range(1, total_level + 1):
    for k in range(total_level - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")  # end=""表示不换行
    print("")
print("---------------------------")
for i in range(1, total_level + 1):
    for k in range(total_level - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 1 - 1 or i == total_level:
            print("*", end="")  # end=""表示不换行
        else:
            print(" ", end="")
    print("")
