# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午11:30
# @Note     :   仅作学习使用--禁止传播，违者必究✅

str_a = 'hello.txt'
list_a = ['jack', 'tom', 'mary']
tuple_a = ('hsp', 'tim')
set_a = {"red", 'black'}
dict_a = {'001': "小倩", '002': "红糖"}

"""
list([iterable]}):
iterable 可以是序列，支持迭代的容器或其他可迭代对象
就是将指定容器转成列表
"""
print("-" * 60)
print(f"str_a转成list:{list(str_a)}")
print(f"tuple_a转成list:{list(tuple_a)}")
print(f"set_a转成list:{list(set_a)}")
print(f"dict_a转成list:{list(dict_a)}")

# str(容器): 将指定的容器转成字符串
print("-" * 60)
print(f"list_a转成str:{str(list_a)} 类型:{type(str(list_a))}")
print(f"tuple_a转成str:{str(tuple_a)} 类型:{type(str(tuple_a))}")
print(f"set_a转成str:{str(set_a)} 类型:{type(str(set_a))}")
print(f"dict_a转成str:{str(dict_a)} 类型:{type(str(dict_a))}")

"""
tuple([iterable]):
iterable 可以是序列，支持迭代的容器或其他可迭代对象
就是将指定容器转成元组
"""
print("-" * 60)
print(f"str_a转成tuple:{tuple(str_a)}")
print(f"list_a转成tuple:{tuple(list_a)}")
print(f"set_a转成tuple:{tuple(set_a)}")
print(f"dict_a转成tuple:{tuple(dict_a)}")


"""
set([iterable]):
iterable 可以是序列，支持迭代的容器或其他可迭代对象
就是将指定容器转成集合
"""
print("-" * 60)
print(f"str_a转成set:{set(str_a)}")
print(f"list_a转成set:{set(list_a)}")
print(f"tuple_a转成set:{set(tuple_a)}")
print(f"dict_a转成set:{set(dict_a)}")
