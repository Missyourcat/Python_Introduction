# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/29 下午1:58
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 循环从键盘输入5个成绩，保存到列表，并输出
lst = list()
for i in range(0, 5):
    score = float(input(f"第{i + 1}个成绩:"))
    lst.append(round(score, 2))
print(lst)
