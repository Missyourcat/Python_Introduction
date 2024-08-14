# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午8:14
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
有一个列表:白眉鹰王，金毛狮王，紫衫龙王，青翼蝠王，猜名字游戏：
从键盘输入一个名称，判断列表中是否包含此名称[顺序查找]
找到了，提示找到，并返回下表
"""
names_list = ["白眉鹰王", "金毛狮王", "紫杉龙王", "青翼蝠王", "金毛狮王", "金毛狮王"]
find_name = "金毛狮王"


# 使用list.index完成查找
# res_index = names_list.index(find_name)
# print("res_index:", res_index)
def seq_search(my_list, find_val):
    """
    功能:顺序查找指定的元素
    :param my_list: 传入的列表
    :param find_val: 查找的元素
    :return: 如果查找到则返回对应的索引下标，否则返回-1
    """
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            print(f"恭喜,找到对应值{find_val} 下标是 {i}")
            return i
            break
    else:
        return -1


print(seq_search(names_list, find_name))

"""
如果一个列表中有多个要查找的元素/值，比如前面的列表有两个金毛狮王
怎样才能把满足查询条件的元素的下标，都返回
"""


def seq_reach_2(my_list, find_val, index_num):
    count = 0
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            print(f"恭喜,找到对应值{find_val} 下标是 {i}")
            index_num.append(i)
            count += 1
    if count == 0:
        print("没找到")


index_list = list()
print("分割".center(30, "-"))
seq_reach_2(names_list, find_name, index_list)
print(index_list)
