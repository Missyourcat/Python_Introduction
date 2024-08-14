# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午11:24
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 出票系统：根据淡旺季的月份和年龄，打印票价
"""
4-10旺季:
    成人(18-60):60
    儿童(<18):半价
    老人(>60):1/3
淡季:
    成人:40
    其他:20
"""
datetime = int(input("月份:"))
age = int(input("年龄:"))
if 4 <= datetime <= 10:
    price = 60
    if 0 < age <= 100:
        if age > 60:
            print(f"{price / 3}元/张")
        elif age < 18:
            print(f"{price / 2}元/张")
        elif 18 <= age <= 60:
            print(f"{price}元/张")
        else:
            print("异常")
    else:
        print("请输入正确年龄")
else:
    price = 40
    if 0 < age <= 100:
        if 18 <= age <= 60:
            print(f"{price}元/张")
        else:
            print(f"{price / 2}元/张")
    else:
        print("请输入正确年龄")
