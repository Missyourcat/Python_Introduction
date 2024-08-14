# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 上午10:16
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
基础数据类型注解
1.  xx: xxx: 对xx进行类型注释，标注n1的类型为int
2.  给出的值类型和标注类型不一致，PyCharm会给出黄色警告
"""
n1: int = 10
n2: float = 30.1
is_pass: bool = True
name: str = '盐池县'

"""
实例对象型注解
"""


class Cat:
    pass


cat: Cat = Cat()

"""
容器类型注解
"""
my_list: list = [1, 2, 3]
my_tuple: tuple = ('A', 'B', 'C')
my_set: set = {'A', 'B', 'A'}
my_dict: dict = {'name': 'A', "age": 18}
"""
容器详细类型注解
元组类型设置详细注解，需要每个元素类型都标注一下
字典类型设置类型注解，需要设置两个类型，即[key类型,value类型
"""
my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[str, str, str, float] = ('A', 'B', 'C', 10.0)
my_set2: set[str] = {'A', 'B', 'A'}
my_dict2: dict[str, int] = {'name': 'A', "age": 10}

"""
注释中使用注解
"""
n3 = 89.3  # type: float
my_list3 = [100, 200, 300]  # type:list[int]
email = "@qq.com"  # type: str
