# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午9:17
# @Note     :   仅作学习使用--禁止传播，违者必究✅

import random
# 随机生成1-100的一个数，直到生成97,统计次数
n = random.randint(1, 100)
print(n)
count = 1
while n != 97:
    n = random.randint(1, 100)
    print(n)
    count += 1
    if n == 97:
        print("总共", count, "次")
        break
else:
    print("总共", count, "——次")

