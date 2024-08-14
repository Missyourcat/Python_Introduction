# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/14 上午2:11
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import time


def operation_menu():
    print()
    print("请选择操作".center(60, '='))
    print(f"1 查 看 当 前 登 录 用 户")
    print(f"1 查 看 登 录 日 志")
    print(f"3 退 出 系 统")


def record_log(user, info):
    with open('log.txt', 'a', encoding='utf-8') as f:
        s = f'登陆用户: {user}, {info} 登陆时间: {time.strftime("%m-%d %H:%M:%S", time.localtime(time.time()))} \n'
        f.write(s)


def read_log():
    with open('log.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    user = input("请输入用户名:")
    pwd = input("请输入密 码:")
    if user in ['smith', 'tom', 'py'] and pwd == '888':
        record_log(user, "登陆成功")
        while True:
            operation_menu()
            key = input("强输入你的选择")
            if key == '1':
                print(f"当前登陆用户: {user}")
            elif key == '2':
                read_log()
            elif key == '3':
                print("退出程序")
                break
            else:
                print("输入有误")
    else:
        record_log(user, '登陆失败')
        print('账号密码有错误')
