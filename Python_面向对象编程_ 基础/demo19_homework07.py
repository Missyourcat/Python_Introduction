# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
有个人Tom 设计他的成员变量，成员方法，可以进行电脑猜拳，电脑每次都会随机生成0 1 2
0 表示 石头 1 表示剪刀 2 表示 布
并要可以显示tom的输赢次数(清单)

"""
import random


class Person:
    computer_count = 0
    player = 0

    def play(self, value):

        computer = int(random.choice([0, 1, 2]))
        if value == 0 and computer == 2:
            self.computer_count += 1
            return "机器胜利"
        elif value == 1 and computer == 0:
            self.computer_count += 1
            return "机器胜利"
        elif value == 2 and computer == 1:
            self.computer_count += 1
            return "机器胜利"
        elif value == 0 and computer == 1:
            self.player += 1
            return "玩家胜利"
        elif value == 1 and computer == 2:
            self.player += 1
            return "玩家胜利"
        elif value == 2 and computer == 0:
            self.player += 1
            return "玩家胜利"
        else:
            return "平局"


one = Person()
count = 1
while count <= 5:
    print(f"第 {count} 场 {one.play(int(input("请玩家出示")))}")
    count += 1
print(f"玩家胜利{one.player}次 失败{one.computer_count}次")
