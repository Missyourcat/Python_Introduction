# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午10:29
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 判断一个年份是否是闰年，闰年的条件是符合下面二者之一
"""
(1)年份能被4整除，但不能被100整除
(2)能被400整除
"""
year = 2000
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
