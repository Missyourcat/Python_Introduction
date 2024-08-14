# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午10:31
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# f1是个函数
def f1():
    for i in range(1, 5):
        if i == 3:
            return  # 跳出函数
            # break  # 结束循环
            # continue  # 结束本次循环
        print("i =", i)
    print("for结束了。。。")


# 调用f1函数
f1()
