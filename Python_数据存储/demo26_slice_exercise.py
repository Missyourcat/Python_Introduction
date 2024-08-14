# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/7 上午12:57
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
定义列表list_name = ["jack", "lisa", "ok", "poul", "smith", "kobe"]
取出前三个名字
取出后三个名字，并且保证原来顺序
"""
list_name = ["jack", "lisa", "ok", "poul", "smith", "kobe"]
list_name_slice_A = list_name[0:3:1]
print(list_name_slice_A)

list_name_slice_B = list_name[-1:-4:-1]

function_A = list_name_slice_B[::-1]
list_name_slice_B.reverse()
function_B = list_name_slice_B
function_C = list_name[-3::]
print(function_A)
# print(list_name_slice_B)
print(function_B)
print(function_C)


