# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午9:33
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 1-100以内的数求和，求出当和第一次大于20的当前控制循环的变量值是多少

sum = 0
for i in range(1, 101):
    sum += i
    if sum > 20:
        break
print(i)
