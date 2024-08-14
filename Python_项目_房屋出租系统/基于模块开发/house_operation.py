# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午11:00
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from my_tools import *

"""
提供对房屋的各种操作
"""


def main_menu():
    """
    显示主菜单，让用户选择
    :return:
    """
    print()
    print("房屋出租系统".center(32, "="))
    print("\t\t\t1 新 增 房 源")
    print("\t\t\t2 查 找 房 屋")
    print("\t\t\t3 删 除 房 屋 信 息")
    print("\t\t\t4 修 改 房 屋 信 息")
    print("\t\t\t5 房 屋 列 表")
    print("\t\t\t6 退      出")


def list_houses():
    """
    显示房屋列表
    :return:
    """
    print("房屋列表".center(60, "="))
    # 遍历HOUSES列表
    for_house(HOUSES)
    print("房屋列表显示完毕".center(60, "="))


def add_house():
    """
    添加房屋信息
    :return:
    """
    print("添加房屋".center(32, "="))
    name = input("姓名: ")
    phone = input("电话: ")
    address = input("地址: ")
    rent = int(input("租金: "))
    state = input("状态: ")
    # 分配ID
    global ID_COUNTER  # 使用全局变量
    ID_COUNTER += 1
    # 构建房屋信息对应的字典，加入到全局houses列表
    house = {"id": ID_COUNTER, "name": name, "phone": phone, "address": address, "rent": rent, "state": state}
    HOUSES.append(house)
    print("添加房屋成功".center(32, "="))


def del_house():
    """
    根据id删除房屋信息
    :return:
    """
    print("删除房屋信息".center(32, "="))
    del_id = int(input("请输入待删除房屋的编号(-1推出): "))
    if del_id == -1:
        print("放弃删除房屋信息".center(32, "="))
        return
        # 让用户确认删除
    choice = read_confirm_select()
    if choice == 'y':
        # 去HOUSES列表查找是否存在该房屋[字典]
        house = find_by_id(del_id, HOUSES)
        if house:
            HOUSES.remove(house)
            print("删除房屋成功".center(32, "="))
        else:
            print("房屋编号不存在，删除失败".center(32, "="))
    else:
        print("放弃删除房屋信息".center(32, "="))


def exit_program():
    """
    退出系统
    :return:
    """
    choice = exit_confirm_select()
    if choice == 'y':
        print("你退出了程序，欢迎下次使用")
        return True
    else:
        return False


def find_house():
    print("查找房屋信息".center(60, "="))
    find_id = int(input("请输入要查找的id: "))
    house = find_by_id(find_id, HOUSES)
    if house:
        for_house(house)
    else:
        print("查找的房屋信息不存在".center(60, "="))


def fix_house():
    """
    修改房屋信息
    :return:
    """
    print("修改房屋信息".center(32, "="))
    fix_id = int(input("请选择修改房屋编号(-1表示退出)： "))
    if fix_id == -1:
        print("放弃修改房屋信息".center(32, "="))
        return
    find_house = find_by_id(fix_id, HOUSES)

    if not find_house:
        print("没有要修改的房屋信息".center(32, "="))
        return
    # name = input(f"姓名({find_house['name']}): ")
    # phone = input(f"电话({find_house['phone']}): ")
    # address = input(f"地址({find_house['address']}): ")
    # rent = input(f"租金({find_house['rent']}): ")
    # state = input(f"状态({find_house['state']}): ")
    # if len(name) > 0:
    #     find_house['name'] = name
    # if len(phone) > 0:
    #     find_house['phone'] = phone
    # if len(address) > 0:
    #     find_house['address'] = address
    # if len(rent) > 0:
    #     find_house['rent'] = rent
    # if len(state) > 0:
    #     find_house['state'] = state
    find_house['name'] = read_str(f"姓名({find_house['name']}): ", find_house['name'])
    find_house['phone'] = read_str(f"电话({find_house['phone']}): ", find_house['phone'])
    find_house['address'] = read_str(f"地址({find_house['address']}): ", find_house['address'])
    find_house['rent'] = read_str(f"租金({find_house['rent']}): ", find_house['rent'])
    find_house['state'] = read_str(f"状态({find_house['state']}): ", find_house['state'])

    print("房屋信息修改成功".center(32, "="))


"""
全局变量 即houses,存放所有的房屋信息
"""
HOUSES = [{"id": 1, "name": "tim", "phone": "113", "address": "海淀", "rent": 800, "state": "未出租"}]
ID_COUNTER = 1
