# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/10 上午12:06
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# import math
# import random
# # import math, random
# # 得到一个数的绝对值
# print(math.fabs(-11.2))
# # 从列表中随机返回一个元素
# print(random.choice(['apple', 'pear', 'banana']))

# # from 模块 import 函数，类，变量。。
# from math import fabs  # 导入math模块的fabs函数
# print(fabs(-11.2))

# # 导入模块的全部功能
# from math import *
# print(fabs(-123))
# print(sqrt(9))

# import 模块 as 别名
import random as r
# from 模块 import 函数，类，变量。。 as 别名
from math import fabs as fa
print(r.choice([100, 200, 300]))
print(fa(-9.2))
