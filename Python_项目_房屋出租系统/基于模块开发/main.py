# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午11:00
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
出租系统的主程序
"""
from house_operation import *


def main():
    """
    这是主函数，程序的执行入口
    :return:
    """
    # main_menu函数表示主菜单
    # 循环显示菜单
    while True:
        main_menu()
        key = input("请输入你的选择(1-6):")
        if key in ["1", "2", "3", "4", "5", "6"]:
            if key == "1":
                add_house()
            elif key == "2":
                find_house()
            elif key == "3":
                del_house()
            elif key == "4":
                fix_house()
            elif key == "5":
                list_houses()
            elif key == "6":
                choice = exit_program()
                if choice == True:
                    break


if __name__ == '__main__':
    main()
