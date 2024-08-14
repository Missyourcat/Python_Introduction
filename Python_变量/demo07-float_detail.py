# @System   :   Arch Linux
# @Author   :   MR.申
# @File     :   demo02-快捷键|转义字符.py
# @Time     :   2024/7/6 下午3:50
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import sys
from decimal import Decimal

n1 = 4.5
n2 = -3.6
print("n1 = ", n1)
print("n2 = ", n2)

# 浮点类型的表示形式
n3 = 5.12
n4 = .512
print("n3 = ", n3)
print("n4 = ", n4)

# 科学计数法形式：如：5.12e2 5.12E-2
n5 = 5.12e2
n6 = 5.12E-2
print("n5 = ", n5)
print("n6 = ", n6)
print(sys.float_info.max, "-", sys.float_info.min)

# 浮点类型计算后，存在精度的损失，可以使用Decimal类进行精准计算
# 需要导入Decimal类from decimal import Decimal

b = 8.1 / 3  # 2.7
print("b = ", b)

b = Decimal("8.1") / Decimal("3")  # 2.7
print("b = ", b)
