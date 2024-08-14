# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 上午3:28
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from house_service import *
from utility import *

"""
界面层，显示界面，接受用户输入，调用业务层的方法
"""


class HouseView:
    # 定义属性house_operation
    house_operation: HouseService = HouseService()

    def update_house(self):
        """
        修改的界面，输入新的数据，修改对应的房屋信息即可
        :return:
        """
        print("修改房屋信息".center(32, "="))
        fix_id = int(input("请选择修改房屋编号(-1表示退出)： "))
        if fix_id == -1:
            print("放弃修改房屋信息".center(32, "="))
            return
        find_house = self.house_operation.find_by_id(fix_id)
        if not find_house:
            print("没有要修改的房屋信息".center(32, "="))
            return
        find_house.name = Utility.read_str(f"姓名({find_house.name}): ", find_house.name)
        find_house.phone = Utility.read_str(f"电话({find_house.phone}): ", find_house.phone)
        find_house.address = Utility.read_str(f"地址({find_house.address}): ", find_house.address)
        find_house.rent = Utility.read_str(f"租金({find_house.rent}): ", find_house.rent)
        find_house.state = Utility.read_str(f"状态({find_house.state}): ", find_house.state)

    def find_house(self):
        """
        显示查找的页面，接收用户输入的id,返回house
        :return:
        """
        print("查找房屋信息".center(60, "="))
        find_id = int(input("请输入要查找的id: "))
        house = self.house_operation.find_by_id(find_id)
        if house:
            print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)\t\t")
            print(house)
        else:
            print("查找的房屋信息不存在".center(60, "="))

    def exit_sys(self):
        """
        退出系统(需求确认)
        :return:
        """
        key = Utility.read_confirm_select()
        if key == 'y':
            return True
        else:
            return False

    def del_house(self):
        """
        删除房屋界面，接收用户输入
        :return:
        """
        print("删除房屋信息".center(32, "="))
        del_id = int(input("请输入待删除房屋的编号(-1推出): "))
        if del_id == -1:
            print("放弃删除房屋信息".center(32, "="))
            return
            # 让用户确认删除
        choice = Utility.read_confirm_select()
        if choice == 'y':
            if self.house_operation.del_by_id(del_id):
                print("删除房屋成功".center(32, "="))
            else:
                print("房屋编号不存在，删除失败".center(32, "="))
        else:
            print("放弃删除房屋信息".center(32, "="))

    def add_house(self):
        """
        显示添加界面，受到用户的输入，构建house对象
        :return:
        """
        print("添加房屋".center(32, "="))
        name = input("姓名: ")
        phone = input("电话: ")
        address = input("地址: ")
        rent = int(input("租金: "))
        state = input("状态: ")

        # 构建房屋信息对象，加入到全局houses列表
        new_house = House(0, name, phone, address, rent, state)
        self.house_operation.add(new_house)
        print("添加房屋成功".center(32, "="))

    def list_houses(self):
        """
        显示房屋列表
        :return:
        """
        print("房屋列表".center(60, "="))
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态(未出租/已出租)\t\t")
        houses = self.house_operation.get_house()
        for house in houses:
            print(house)
        print("房屋列表显示完毕".center(60, "="))

    def main_menu(self):
        """
        显示主菜单
        :return:
        """
        while True:
            print()
            print("房屋出租系统".center(32, "="))
            print("\t\t\t1 新 增 房 源")
            print("\t\t\t2 查 找 房 屋")
            print("\t\t\t3 删 除 房 屋 信 息")
            print("\t\t\t4 修 改 房 屋 信 息")
            print("\t\t\t5 房 屋 列 表")
            print("\t\t\t6 退      出")
            key = input("请输入你的选择(1-6):")
            if key in ["1", "2", "3", "4", "5", "6"]:
                if key == "1":
                    self.add_house()
                elif key == "2":
                    self.find_house()
                elif key == "3":
                    self.del_house()
                elif key == "4":
                    self.update_house()
                elif key == "5":
                    self.list_houses()
                elif key == "6":
                    if self.exit_sys():
                        break
