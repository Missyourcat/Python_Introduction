# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午5:06
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# for_else案例
nums = [1, 2, 3]
for i in nums:
    print("你好", i)
else:
    print("结束")
for i in nums:
    print("你好", i)
    if i == 2:
        break
else:
    print("结束")
