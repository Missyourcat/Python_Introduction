# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/10 上午12:17
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
没有__all__时，会导入所有功能
使用了__all__ = ['ok'] 在其它文件使用 from xxx import * 只会导入ok
import 模块 方式不受__all__的限制
"""
__all__ = ['ok', 'hi']


def hi():
    print("hi 1")


def ok():
    print("ok 1")


if __name__ == "__main__":
    hi()
    print(__name__)
