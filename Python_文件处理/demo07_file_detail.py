# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午1:16
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import time

# # f.flush() :刷新流的写入缓冲区
# f = open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/abc.txt", 'w', encoding='utf-8')
# f.write("你好1")
# f.write("你好2")
# f.write("你好3")
#
# # 测试f.flush()将缓冲区数据刷新，写入文件
# f.flush()
# print("---等待---")
# time.sleep(10)
# print("---等待 end---")

# f.close():刷新并关闭此流，也就是f.close()内置的flush功能

# with open() as f :在处理文件对象时，子句体结束后，文件会自动关闭

# with open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/abc.txt", 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line, end='')
# print("\n文件是否关闭", f.closed)

"""
关于目录分隔符，
在win下 / 和 // 都可以
linux/unix 是 /
因此建议目录分隔符，为了兼容linux和windows都使用 /
"""
