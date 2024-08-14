# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/21 下午10:29
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 定义两个变量int类型，判断二者之和，是否能被3又能被5整除，打印提示信息
numb1 = 12
numb2 = 31
if (numb1 + numb2) % 3 == 0 and (numb1 + numb2) % 5 == 0:
    print(f"{numb1} + {numb2} = {numb1 + numb2},可以被3和5整除")
else:
    print(f"{numb1} + {numb2} = {numb1 + numb2},不可以被3和5整除")
