# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午10:38
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class GrandPa:
    name = "大头爷爷"
    hobby = "旅游"


class Father(GrandPa):
    name = "大头爸爸"
    age = 39


class Son(Father):
    name = "大头儿子"


son = Son()
print(f"son.name: {son.name} son.age: {son.age} son.hobby: {son.hobby}")
