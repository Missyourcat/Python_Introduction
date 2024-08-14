# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午9:13
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 在第一题的基础上，使用二分查找，查找是否有8这个数
# 如果有，则返回对应的下标，如果没有，返回-1
from random import randrange

# 随机生成10个整数(1-100的范围)保存到列表，使用冒泡排序，对其进行从大到小排序
num_list = list()

for ele in range(10):
    num_list.append(randrange(1, 101))
print(num_list)


def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] < my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}次排序:{my_list}")


bubble_sort(num_list)


def binary_sort(my_list, find_val):
    left_index = 0
    right_index = len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] < find_val:
            right_index = mid_index - 1
        elif my_list[mid_index] > find_val:
            left_index = mid_index + 1
        else:
            find_index = mid_index
            break
    return find_index


find_value = 8
res_index = binary_sort(num_list, find_value)
if res_index == -1:
    print("没找到")
else:
    print("找到了，下标", res_index)
