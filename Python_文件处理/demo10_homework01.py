# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午1:53
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
1.实现登录验证，如果用户名是列表中的元素['smith','tom','py'],密码'888'则登陆成功，否则失败
2.不管登陆是否成功，都需要在文件中记录登录的信息
3.登陆成功，可以看到相应的操作菜单提示
"""
import time

user_list = ['smith', 'tom', 'py']
while True:
    name = input("请输入用户名:")
    pwd = input("请输入密 码:")
    if name in user_list and pwd == '888':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f"登录用户: {name}, 登陆成功 登陆时间:{time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))} \n")
        while True:
            print("请选择操作".center(60, '='))
            print(f"1 查 看 当 前 登 录 用 户")
            print(f"1 查 看 登 录 日 志")
            print(f"3 退 出 系 统")
            choice = int(input("请输入你的选择:"))
            if choice == 1:
                print(f"当前登陆用户: {name}")
            elif choice == 2:
                with open('log.txt', 'r', encoding='utf-8') as f:
                    for line in f:
                        print(line, end='')
            elif choice == 3:
                break
            else:
                print("输入错误")
        break
    else:
        print(f"密码或者账号错误")
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f"登录用户: {name}, 登陆失败 登陆时间:{time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))}\n")
