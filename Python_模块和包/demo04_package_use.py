# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/10 下午10:53
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# # 导入包下的模块
# import demo04_package.module01
# import demo04_package.module02
#
# # 使用导入的模块
# demo04_package.module01.hi()
# demo04_package.module02.ok()

# # from 包名 import 模块， 这种方式导入，在使用时，模块.功能 , 不用带包名
# from demo04_package import module01
#
# # 直接使用模块名.功能名
# module01.hi()

# # 导入包的模块的指定函数，类，变量
# from demo04_package.module01 import hi
# # 直接使用功能名调用
# hi()

# # from 包名.模块 import * : 表示导入包的模块的所有功能
# from demo04_package.module01 import *
# hello.txt()

# # __init__.py 通过 __all__ 控制允许导入的模块
# from demo04_package import *
# module02.ok()
# # module01.hi()  # 引入限制了module01模块导入,因此不能使用

# # __all__ = ['module02'] 不能限制 下面的导入形式
# import demo04_package.module02
# import demo04_package.module01
#
# demo04_package.module01.hi()
# demo04_package.module02.ok()

"""
包可以有多个层级
"""
from math import fabs

# # 使用方式1
# import demo04_package.package_02.module03
# demo04_package.package_02.module03.cal(10, 20)

# # 使用方式2
# from demo04_package.package_02.module03 import cal
# cal(30, 60)
#
# # 使用方式3
# from demo04_package.package_02 import module03
# module03.cal(10, 10)

print(fabs(10, 1))
