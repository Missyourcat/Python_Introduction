# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午9:23
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
定义Account类
1.Account 类要求具有属性:姓名(2-4位),余额(必须>20),密码(必须是六位)，如果不满足，则给出提示信息，并给默认值
2.通过set_xxx的方法给Account的属性赋值
3.编写方法query_info()接收姓名和密码，如果姓名和密码正确，返回该账号信息
"""


class Account:
    __name = None
    __balance = None
    __pwd = None

    def set_name(self, name):
        if 2 <= len(name) <= 4:
            self.__name = name
        else:
            print("名字长度不再2-4之间")

    def set_balance(self, balance):
        if 20 < balance:
            self.__balance = balance
        else:
            print("余额不足")

    def set_pwd(self, pwd):
        if len(pwd) == 6:
            self.__pwd = pwd
        else:
            print("密码不是6位")

    def query_info(self, name, pwd):
        if name == self.__name and pwd == self.__pwd:
            return f"账户信息{self.__name} {self.__balance}"
        else:
            return f"请输入正确的名字和密码"


account = Account()
account.set_name("ok")
account.set_pwd("123465")
account.set_balance(200)
print(account.query_info('ok', '123465'))
