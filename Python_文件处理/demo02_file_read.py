# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午12:26
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 打开文件
f = open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/hello.txt", 'r', encoding='utf-8')
#
# # 读取方式1:read(),一次返回整个文件的内容
# content = f.read()
# # 关闭文件，释放文件占用的系统资源
# print(content)

# # 读取方式2:f.readline(),注意readline,字符串末尾保留换行符
# line1 = f.readline()  # 自动加一个换行符
# line2 = f.readline()
# print(f"第一行数据:{line1}")
# print(f"第一行数据:{line2}")
# f.close()
# # 循环读取整个文件，一行行的读取
# while True:
#     line_content = f.readline()
#     if line_content == "":
#         break
#     print(line_content, end="")
# f.close()

# # 读取方式3:f.readlines()列表形式读取文件中的所有行
# lines = f.readlines()
# print(f"lines的类型是 {type(lines)}")
# print(f"lines的内容是 {lines}")
# for line in lines:
#     print(line, end='')
# f.close()

# 读取方式4:for line in f形式读取文件
for line in f:
    print(line, end='')
f.close()
