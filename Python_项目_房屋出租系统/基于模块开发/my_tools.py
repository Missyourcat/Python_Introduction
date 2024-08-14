# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午11:46
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
这里编写工具函数，供程序员使用
"""


def read_confirm_select():
    """
    确认用户输入的是(Y/N),不区分大小写
    如果用户输入不是Y/N 就反复输入
    :return:
    """
    while True:
        key = input("请输入你的选择(Y/N), 请确认选择:")
        if key.lower() == 'y' or key.lower() == 'n':
            break
    return key.lower()


def exit_confirm_select():
    """
    确认用户输入的是(Y/N),不区分大小写
    如果用户输入不是Y/N 就反复输入
    :return:
    """
    key = input("请输入你的选择(Y/N), 请确认选择:")
    while True:
        if key.lower() == 'y' or key.lower() == 'n':
            break
        else:
            key = input("选择错误，请从新输入: ")
    return key.lower()


def for_house(HOUSES):
    """
    遍历列表/字典
    如果为列表遍历数据
    如果为字典展示value值
    :param HOUSES:
    :return:
    """
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)\t\t")
    if type(HOUSES) is list:
        for house in HOUSES:
            # 取出HOUSES的values
            for value in house.values():
                print(value, end="\t\t")
            print()
    else:
        for value in HOUSES.values():
            print(value, end="\t\t")
        print()


def find_by_id(find_id, houses_list):
    """
    根据输入的find_id 返回对应的房屋信息（字典），如果没有就返回None
    :param houses_list:
    :param find_id:
    :return:
    """
    # 遍历HOUSES列表
    for house in houses_list:
        if house["id"] == find_id:
            return house
    # 如果没有return,默认值None
    return None


def read_str(tip, default_val):
    """
    读取用户输入，如果用户没有输入内容，则返回default_val
    :param tip: 提示信息
    :param default_val:用户指定
    :return:
    """
    str = input(tip)
    if len(str) > 0:
        return str
    else:
        return default_val
