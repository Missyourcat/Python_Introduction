# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午9:25
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 它会终结最近的外层循环，如果循环有可选的else子句，也会跳过该子句
count = 0
while True:
    print("hi while")
    count += 1
    if count == 3:
        break
    while True:
        print("ok while")
        break
else:
    print("hello.txt while")

# 如果一个for循环被break终结，该循环的控制变量会保持当前值
nums = [1, 2, 3, 4, 5]
for i in nums:
    if i > 3:
        break
print("i=", i)
