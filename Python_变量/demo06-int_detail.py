# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/6 下午3:21
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import sys

# int类型的细节
# python中，int可以表示很大的数
n3 = 9 ** 88  # 9的88次方
print("n3 = ", n3, type(n3))
# n4 = 9 ** 8888  # 9的8888次方
# print("n4 = ", n4, type(n4))

# python的整数有十进制， 十六进制， 八进制， 二进制表示
print(10)
# 十六进制
print(0x10)
# 八进制
print(0o10)
# 二进制
print(0b10)

# 字节数随着数字的增大而增大 增量为四个字节 1byte(字节)=8bit(位)
I1 = 0
I2 = 1
I3 = 2
I4 = 2 ** 15
I5 = 2 ** 30
I6 = 2 ** 128
# 在python中，可以通过sys.getsizeof 返回对象(数据)的大小(按照字节单位返回)

print(I1, sys.getsizeof(I1), "类型", type(I1))
print(I2, sys.getsizeof(I2), "类型", type(I2))
print(I3, sys.getsizeof(I3), "类型", type(I3))
print(I4, sys.getsizeof(I4), "类型", type(I4))
print(I5, sys.getsizeof(I5), "类型", type(I5))
print(I6, sys.getsizeof(I6), "类型", type(I6))

