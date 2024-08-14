# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午10:08
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# list越界异常
names_list = ['jordan', 'kobe', 'james', " Messi"]
i = 0
while i <= len(names_list):
    print(f"names_list[{i}]={names_list[i]}")
    i += 1
