# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午1:28
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
将一张图片/一首歌 拷贝到另一个目录下，要求使用read()和write()原生方法完成
1.打开源文件，读取源文件的数据
2.打开目标文件，把读取到的数据写入到目标文件
3.音频/图片是二进制文件，需要以二进制的方式打开
"""
# 源文件
f_src_path = '/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/图片/system.png'
# 目标文件
# f_dst_path = '/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/new.png'
f_dst_path = '/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/一级目录/new2.png'

# # rb 读取 二进制
# f_src = open(f_src_path, 'rb')
# # 读取源文件的数据
# data = f_src.read()
# # print(data)
# # 打开目标文件
# f_dst = open(f_dst_path, 'wb')
# f_dst.write(data)
# # 关闭文件
# f_src.close()
# f_dst.close()
# print("拷贝成功")

# 使用with子句的方式完成文件的拷贝（读取一行数据就写入）
with open(f_src_path, 'rb') as f_src:
    with open(f_dst_path, 'wb') as f_dst:
        for data in f_src:
            f_dst.write(data)
print("拷贝ok")