# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/19 下午4:28
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# Python缩进用于界定代码块的
if 4 > 1:
    print("ok1")
    print("ok2")
print("ok3")

# 缩进前后没有要求，但是每个代码块应具有相同的缩进长度（TAB或者相同个数的空格）
# 较短的缩进对较长的缩进有包含关系
if 100 > 20:
    print("ok4")
    print("ok5")
    if 9 < 2:
        print("ok6")
