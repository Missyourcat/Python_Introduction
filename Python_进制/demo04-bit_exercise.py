# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/19 下午4:09
# @Note     :   仅作学习使用--禁止传播，违者必究✅

a = 1 >> 2
b = -1 >> 2
c = 1 << 2
d = -1 << 2
print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)

print(~2)
print(2 & 3)
print(2 | 3)
print(~-5)  # 1000 1001 -> 1111 0110 -> 1111 0111 -> 0000 1000
print(13 & 7)
print(5 | 4)
print(-3 ^ 3)
# 1000 0011 -> 1111 1100 -> 1111 1101 -> 1111 1110 -> 1111 1101 -> 1000 0010
#                           0000 0011
