# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午12:22
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 如果要创建一个文件，只需要以mode = 'w'形式打开文件，如果不存在，系统就会创建该文件
# encoding 是关键字参数，不能少
f1 = open("/home/Missyourcat/learn/Python_code/pythonProject/Python_文件处理/素材/hi.txt", 'w', encoding='utf-8')
print(f"文件创建成功 类型是 {type(f1)}")
