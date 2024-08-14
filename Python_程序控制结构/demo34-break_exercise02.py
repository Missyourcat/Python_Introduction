# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午9:33
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 实现登录验证，有三次机会，如果用户名为“张无忌”，密码"888"提示登录成功，否则提示还有几次机会，请使用for+break完成
change = 3
for i in range(change):
    name = input("用户名：")
    password = int(input("密 码:"))
    if name == "张无忌" and password == 888:
        print("登录成功")
        break
    else:
        print(f"还有{change - 1 - i}次机会")
