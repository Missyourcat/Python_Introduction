# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 上午3:37
# @Note     :   仅作学习使用--禁止传播，违者必究✅
from house import *

"""
业务层：提供对房屋操作方法
"""


class HouseService:
    # 定义属性houses类别，存放房屋信息（对象）
    houses = []
    # 定义id_counter
    id_counter = 1

    def __init__(self):
        house = House(1, 'tim', "118", "hd", 800, "未出租")
        self.houses.append(house)

    def get_house(self):
        """
        返回房屋列表
        :return:
        """
        return self.houses

    def add(self, new_house):
        """
        将收到的house添加到houses中
        :param new_house:
        :return:
        """
        self.id_counter += 1
        new_house.id = self.id_counter
        self.houses.append(new_house)

    def find_by_id(self, find_id):
        """
        根据find_id返回对应的house对象，不存在返回None
        :param find_id:
        :return:
        """
        for house in self.houses:
            if house.id == find_id:
                return house

    def del_by_id(self, del_id):
        """
        根据收到的id删除房屋
        :param del_id:
        :return:
        """
        house = self.find_by_id(del_id)
        if house is None:
            return False

        # 找到house就删除
        self.houses.remove(house)
        return True
