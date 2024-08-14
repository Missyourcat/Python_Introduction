# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午6:20
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 打印空心菱形
all = 21
level = int(all / 2) + 1
for i in range(level):
    for j in range(level - 1 - i):
        print(" ", end="")
    for k in range(2 * (i + 1) - 1):
        if k == 0 or k == 2 * (i + 1) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
for x in range(all - level):
    for y in range(x + 1):
        print(" ", end="")
    for z in range(2 * (level - x - 1) - 1):
        if z == 0 or z == 2 * (level - x - 1) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
print("----------------------------------")
i = 0
x = 0
while i < level:
    j = 0
    k = 0
    while j < level - 1 - i:
        print(" ", end="")
        j += 1
    while k < 2 * (i + 1) - 1:
        if k == 0 or k == 2 * (i + 1) - 2:
            print("*", end="")
        else:
            print(" ", end="")
        k += 1
    i += 1
    print("")

while x < all - level:
    y = 0
    z = 0
    while y < 1 + x:
        print(" ", end="")
        y += 1
    while z < 2 * (level - (x + 1)) - 1:
        if z == 0 or z == 2 * (level - (x + 1)) - 2:
            print("*", end="")
        else:
            print(" ", end="")
        z += 1
    x += 1
    print("")
