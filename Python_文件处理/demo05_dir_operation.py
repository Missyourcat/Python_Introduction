# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午12:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import os

# 1.创建一级目录 mkdir一个文件
# if not (os.path.isdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录")):
#     os.mkdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录")
# else:
#     print("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录  目录已存在")

# # 2.创建多级目录 makedirs多个文件
# if os.path.isdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录"):
#     print("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录   已存在")
# else:
#     os.makedirs("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录")

# 3.删除目录
# # 删除单级目录使用rmdir,要求目录为空
# if os.path.isdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录"):
#     os.rmdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录")
# else:
#     print("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录   目录不存在")
# # 删除多级目录使用removedirs,要求目录为空
if os.path.isdir("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录"):
    os.removedirs("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录")
else:
    print("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/二级目录 不存在")
