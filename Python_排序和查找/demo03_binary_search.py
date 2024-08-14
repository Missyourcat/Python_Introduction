# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午8:48
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 请对一个列表(元素从小到大排序的)进行二分查找,输入一个数看看该列表是否存在此数，并且求出下标，如果没有就返回-1
"""
1.找到列表的中间数 mid_val 和 find_val 比较
2.如果 mid_val > find_val，则到mid_val的左边查找
3.如果 mid_val < find_val，则到mid_val的右边查找
4.如果 mid_val == find_val，返回下标
5.不断重复1-4，不断折半，使用while
6.如果while结束，都没有找到，说明find_val没有在列表
"""


def binary_search(my_list, find_val):
    """
    功能:完成二分查找
    :param my_list:要查找的列表
    :param find_val: 要查找的元素 /值
    :return: 如果找到返回对应的下标，否则返回-1
    """
    left_index, right_index = 0, len(my_list) - 1
    fin_index = -1
    while left_index <= right_index:  # 比较的前提
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] > find_val:
            right_index = mid_index - 1
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
        else:
            fin_index = mid_index
            break
    return fin_index


num_list = [1, 8, 10, 89, 1000, 1234]

res_index = binary_search(num_list, 1)
if res_index == -1:
    print("没找到")
else:
    print("找到了,下标为", res_index)
