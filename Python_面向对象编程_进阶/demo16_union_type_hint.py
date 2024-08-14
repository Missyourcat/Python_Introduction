# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:11
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
联合类型注释，a可以是int或者str
如果使用union类型注解，需要导入
"""
from typing import Union

a: Union[int, str] = 100
my_list: list[Union[int, str]] = [100, 200, 300, 'time']


def cal(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


print(f"结果是{cal(10, 10.1)}")
