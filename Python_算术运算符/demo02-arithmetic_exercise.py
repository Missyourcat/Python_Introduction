# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/16 上午1:05
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 1.假如还有97天放假，问：合xx个星期零xx天
# 对7求整除得到多少星期，对7取余得天数
week = 97 // 7
day = 97 % 7
print(str(week) + "个星期,零" + str(day) + "天")

# 2.定义一个变量保存华氏温度，华氏温度转换摄氏温度的公式为：5/9*(华氏温度-32)，请求出华氏温度对应的摄氏温度。[234.5]
hua_shi = 100
she_shi = 5 / 9 * (hua_shi - 32)
print(f"{hua_shi}华氏温度对应的摄氏温度是{she_shi}")
print("%.2f华氏温度对应的摄氏温度是 %.2f" % (hua_shi, she_shi))
