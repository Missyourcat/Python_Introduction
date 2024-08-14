# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午12:14
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
工具类，将工具放到这里
"""


class Utility:
    @staticmethod
    def read_confirm_select():
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

    @staticmethod
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
