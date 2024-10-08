# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午5:47
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
猴子吃桃子问题：有一堆桃子，猴子第一天吃了其中的一半，并再多吃一个！
以后每天猴子都吃其中的一半，然后再多吃一个。
当到第10天时，想再吃时（即还没吃），发现只有1个桃子了。
问：最初多少个桃子？
"""
"""
    思路分析:
    1.day == 10 时，有桃子数1
    2.day == 9 时，day9的桃子数 - (day9的桃子数 / 2 + 1) = day10的桃子数
                    day9的桃子数 / 2 - 1 = day10的桃子数
                    day9的桃子数 = 2 * (day10的桃子数 + 1)
    3.day == 8 时, 2 * (day9的桃子数 + 1)
    4.day == 7 时, 2 * (day8的桃子数 + 1)
    5.day == n 时, 2 * (day(n+1)的桃子数 + 1)
    ....
    10.day == 1 时, 2 * (day2的桃子数 + 1) 
"""


def peach(day):
    if day == 10:
        return 1
    else:
        return 2 * (peach(day + 1) + 1)


print(peach(1))
