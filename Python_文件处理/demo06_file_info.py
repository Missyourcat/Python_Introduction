# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午1:10
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# 获取文件相关信息(大小，创建时间，访问时间，修改时间等)
"""
time.ctime()方法的作用则是将返回的时间戳转化为字符串格式
"""
import os
import time

f_stat = os.stat("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/hello.txt")
print("文件信息".center(32, '='))
print(f"文件大小->{f_stat.st_size} \n"
      f"最近访问时间->{time.ctime(f_stat.st_atime)} \n"
      f"最近修改时间->{time.ctime(f_stat.st_mtime)} \n"
      f"文件创建时间->{time.ctime(f_stat.st_ctime)} \n"
      )
