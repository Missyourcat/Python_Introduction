# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午1:40
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
遍历某个文件夹，判断他们分别是目露还是文件
1.获取文件夹（目录）的所有内容（元素），包含了文件和目录
2.判断是文件还是目录，输出对应的信息
"""
import os

# 指定要查看的目录
# dir_path = '/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理'
# # 获取文件夹(目录)的所有内容（元素）
# content_list = os.listdir(dir_path)
# # print(content_list)
# # 遍历list,输出对应的信息
# for ele in content_list:
#     child_path = dir_path + '/' + ele
#     if os.path.isdir(child_path):
#         print(f"目录:{child_path}")
#     else:
#         print(f"文件:{child_path}")

"""
考虑多级目录-递归操作函数
1.获取文件夹（目录）的所有内容（元素），包含了文件和目录
2.判断是文件还是目录，输出对应的信息
2.1.如果是目录，则输出信息后，在递归处理
2.2.如果是文件，直接给出信息
"""


def print_dir_all_content(dir_path):
    # 获取文件夹(目录)的所有内容（元素）
    content_list = os.listdir(dir_path)
    # print(content_list)
    # 遍历list,输出对应的信息
    for ele in content_list:
        child_path = dir_path + '/' + ele
        if os.path.isdir(child_path):
            print(f"目录:{child_path}")
            print_dir_all_content(child_path)
        else:
            print(f"文件:{child_path}")


print_dir_all_content('/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理')
