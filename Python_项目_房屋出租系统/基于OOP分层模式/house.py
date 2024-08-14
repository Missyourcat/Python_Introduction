# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 上午3:26
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
数据层:House类，一个House对象表示一个房屋信息
"""


class House:
    # 定义属性
    def __init__(self, id, name, phone, address, rent, state):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.rent = rent
        self.state = state

    def __str__(self):
        return f"{self.id}\t\t{self.name}\t\t{self.phone}\t\t{self.address}\t\t{self.rent}\t\t{self.state}"
