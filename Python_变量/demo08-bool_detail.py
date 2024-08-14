# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/6 下午4:01
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# bool类型的基本使用
num1 = 100
num2 = 200
if num1 > num2:
    print("num1 > num2")

# 表示把num1 > num2 的结果赋给result变量
result = num1 > num2
print("result = ", result)

#  看看result的数据类型
print("result的类型", type(result))
print(type(1 > -1))

# 布尔类型可以和其他数据类型进行比较，如数字，字符串
# 在比较时，python会将true视为1,false视为0
b1 = False
b2 = True
print(b1 + 10)
print(b2 - 10)

# b1 = 0:表示赋值
# b1 == 0:表示判断b1是否与0相等

if b1 == 0:
    print("OK")

if b2 == -1:
    print("hi")

# 在Python中，非0被视为真值，0值被视为假值

# if 0:
#     print("哈哈")

if -1:
    print("嘻嘻1")
if 1.1:
    print("嘻嘻2")
if "字符串也行？":
    print("嘻嘻3")

# 课堂练习
if 1:
    print("1...")  # ✅
if -20:
    print("-20")  # ✅
if 1.1:
    print("1.1")  # ✅
if -10.11:
    print("-10.11")  # ✅
if "hello.txt":
    print("hello.txt")  # ✅
num1 = 0
if num1:
    print("哈哈")  # ❌
num2 = -111.11
if num2:
    print("嘻嘻")  # ✅
name = "老师好帅"
if name:
    print(name)  # ✅
