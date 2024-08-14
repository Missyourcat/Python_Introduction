# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/16 上午1:58
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# or运算符的使用
# 短路运算符，只有当第一个为False时才去验证第二个
score = 70

if score <= 60 or score >= 80:
    print("hi~~~~~~~~~`")

a = 1
b = 99
print(a or b)
print((a > b) or b)
print((a < b) or b)

