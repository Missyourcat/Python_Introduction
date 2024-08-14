# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午9:13
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import random

# 随机生成10个整数(1-100的范围)保存到列表，使用冒泡排序，对其进行从小到大排序
num_list = list()

for ele in range(10):
    num_list.append(random.randint(1,100))
print(num_list)


def bubble_sort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
        print(f"第{i + 1}次排序:{my_list}")


bubble_sort(num_list)
