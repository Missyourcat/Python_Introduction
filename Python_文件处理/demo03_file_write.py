# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午12:44
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
mode = 'w' 打开文件，如果文件不存在，会创建，如果文件已经存在，会先截断打开的文件，也就是清空文件内容
如果希望以追加的方式写入，需要mode = 'a'
"""
# f = open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/abc.txt", 'w', encoding='utf-8')
f = open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/abc.txt", 'a', encoding='utf-8')
# i = 1
# while i <= 10:
#     f.write(f"hello,python\n")
#     i += 1
# f.close()
i = 1
while i <= 10:
    f.write(f"hello,abc\n")
    i += 1
f.close()
