# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午5:45
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 如果外层循环次数为m次，内层为n次，则内层循环实际需要执行m*n
# for i in [0, 1]:
#     for j in [0, 1, 2]:
#         print("i=", i, "j=", j)
count = 0
for i in range(2):
    for j in range(3):
        for k in range(4):
            count += 1
            print(f"i={i},j={j},k={k},count={count}")
