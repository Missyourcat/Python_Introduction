# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午6:14
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 汉诺塔
def hanoi(num, a, b, c):
    """

    :param num:盘子数量
    :param a: A柱子
    :param b: B柱子
    :param c: C柱子
    :return:
    """
    if num == 1:
        print("第1个盘从:", a, "->", c)
    else:
        """
        有多个盘，我们认为只有2个，上面所有的盘和最下面的盘
        移动上面的盘子到B柱子，这个过程会借助C柱子
        """
        hanoi(num - 1, a, c, b)
        # 移动最下面的盘
        print(f"第{num}个盘从:", a, "->", c)
        # 把上面所有的盘从B柱子移动到C柱子，这个过程用到A柱子
        hanoi(num - 1, b, a, c)


hanoi(3, "A", "B", "C")
