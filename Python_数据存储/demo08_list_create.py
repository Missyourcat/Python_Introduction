# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/29 下午1:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# [列表元素的表达式 for 自定义变量 in 可迭代变量]
lst1 = [element * 2 for element in range(1, 5)]
print("lst1:", lst1)
lst2 = [ele + ele for ele in "韩顺平"]
print("lst2:", lst2)

# 要求生呈一个列表，内容为[1,4,9,16,25,36,49,64,81,100]
lst3 = [ele ** 2 for ele in range(1, 11)]
print("lst3:", lst3)
