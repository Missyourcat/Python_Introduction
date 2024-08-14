# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午10:37
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
某人有100000元，每经过一次路口，需要交费，规则如下：
当现金>50000时，每次交5%
当现金<=50000时，每次交1000
编程计算该人可以经过多少次路口，使用break+while方式完成
"""
money = 100000.00
count = 0
while True:
    while money > 50000.00:
        money *= 0.95
        count += 1
    while money <= 50000.00:
        money -= 1000.00
        count += 1
        if money < 1000:
            break
    break
print(count, money)

# while True:
#     if money > 50000:
#         count += 1
#         money -= money * 0.05
#     elif money >= 1000:
#         count += 1
#         money -= 1000
#     else:
#         break
# print(count, money)
