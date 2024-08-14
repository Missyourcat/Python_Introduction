# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/16 下午5:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅

name = input("请输入姓名：")
age = input("请输入年龄：")
score = input("请输入成绩：")
print(f"输入信息如下：\nname:{name}\nage:{age}\nscore:{score}")
# 如果进行算法运算，需要进行类型转换
print(10 + float(score))
# 接收数据可以直接转成需要的类型
age = float(input("请输入年龄:"))
print("age的类型是:", type(age))
