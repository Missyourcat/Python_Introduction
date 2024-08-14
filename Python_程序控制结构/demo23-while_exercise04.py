# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午5:33
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 打印1～100之间所有是9的倍数的整数，统计个数及总和
i = 1
max_num = 100
count = 0
sum = 0
while i <= max_num:
    if i % 9 == 0:
        count += 1
        sum += i
    i += 1
else:
    print("个数:",count)
    print("总和:",sum)

