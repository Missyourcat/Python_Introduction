# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午12:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import os
"""
先判断文件存在，如果有则删除
如果没有，则提示"文件不存在，无法删除"
"""
if os.path.exists("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/a.txt"):
    os.remove("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/a.txt")
else:
    print("不存在")
