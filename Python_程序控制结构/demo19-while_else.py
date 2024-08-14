# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午5:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# while_else使用案例
i = 0
# while i < 3:
#     print("你好", i)
#     i += 1
# else:
#     print("i  < 3 不成立 i =", i)

while i < 3:
    print("你好", i)
    i += 1
    if i == 1:
        break
else:
    print("i  < 3 不成立 i =", i)
