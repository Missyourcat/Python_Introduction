# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午7:51
# @Note     :   仅作学习使用--禁止传播，违者必究✅

num_list = [24, 69, 80, 57, 13]
print("排序前".center(32, "-"))
print(num_list)

# 使用sort排序
# num_list.sort()
# print("排序后".center(32, "-"))
# print(num_list)


def bubble_sort(num_list):
    """
    功能:对传入的列表排序-顺序从小到大
    :param num_list:  传入的列表
    :return:
    """
    # for j in range(0, 4):
    #     if num_list[j] > num_list[j + 1]:
    #         num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # x,y=y,x
    # print("第1轮排序的结果：", num_list)
    # for j in range(0, 3):
    #     if num_list[j] > num_list[j + 1]:
    #         num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # x,y=y,x
    # print("第2轮排序的结果：", num_list)
    # for j in range(0, 2):
    #     if num_list[j] > num_list[j + 1]:
    #         num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # x,y=y,x
    # print("第3轮排序的结果：", num_list)
    # for j in range(0, 1):
    #     if num_list[j] > num_list[j + 1]:
    #         num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # x,y=y,x
    # print("第4轮排序的结果：", num_list)
    """
    每一轮比较逻辑是一样的，只需要考虑变化的部分即可，使用外层for循环来处理
    """
    for i in range(0, len(num_list) - 1):
        for j in range(0, len(num_list) - 1 - i):
            if num_list[j] >     num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]  # x,y=y,x
        print("第", i + 1, "轮排序的结果：", num_list)


bubble_sort(num_list)
