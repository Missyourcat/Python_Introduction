# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午10:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
小头儿子 参加pytho考试，他和 大头爸爸 达成承诺:
如果:
成绩为100分时，奖励一辆BMW;
成绩为(80,99],奖励一台iphone13
成绩为(60,80],奖励一台ipad
其它时，什么奖励也没有
请从键盘输入小头儿子的期末成绩，并加以判断
"""
score = int(input("小头儿子的成绩:"))
if 100 >= score >= 0:
    if score == 100:
        print("BMW到账")
    elif 80 < score <= 99:
        print("iphone13到账")
    elif 60 < score <= 80:
        print("ipad到账")
    else:
        print("你要个鸡儿")
else:
    print("不在0-100")
