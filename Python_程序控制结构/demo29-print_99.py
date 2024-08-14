# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午9:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i} * {j} = {i * j}", end="\t")
    print("")
