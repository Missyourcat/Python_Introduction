# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午11:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 参加歌手比赛，如果初赛成绩大于8.0进入决赛，否则提示淘汰。并且根据性别提示进入男子组或女子组。
# 输入成绩和性别，进行判断和输出信息
score = float(input("成绩:"))
if score > 8.0:
    gander = input("性别:")
    if gander == "男":
        print("恭喜入选男子组")
    elif gander == "女":
        print("恭喜入选女子组")
    else:
        print("你是武装直升机还是沃尔玛塑料袋?")
else:
    print("淘汰")
