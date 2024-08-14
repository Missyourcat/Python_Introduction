# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午12:15
# @Note     :   仅作学习使用--禁止传播，违者必究✅

def f1(my_list):
    print(f"f1() my_list:{my_list} 地址是:{id(my_list)}")
    my_list[0] = 'jack'
    print(f"f1() my_list:{my_list} 地址是:{id(my_list)}")


my_list = ['tom', 'marry', 'py']
print(f"my_list:{my_list} 地址是:{id(my_list)}")
f1(my_list)
print(f"my_list:{my_list} 地址是:{id(my_list)}")


def f2(my_tuple):
    print(f"2.f2() my_tuple:{my_tuple} 地址是:{id(my_tuple)}")
    # my_tuple[0] = 'red'
    print(f"3.f2() my_tuple:{my_tuple} 地址是:{id(my_tuple)}")


my_tuple = ('hi', 'ok', 'hello.txt')
print(f"1. my_tuple:{my_tuple} 地址是:{id(my_tuple)}")
f2(my_tuple)
print(f"4. my_tuple:{my_tuple} 地址是:{id(my_tuple)}")


def f3(my_set):
    print(f"2.f3() my_set:{my_set} 地址是:{id(my_set)}")
    my_set.add("<<红楼梦>>")
    print(f"3.f3() my_set:{my_set} 地址是:{id(my_set)}")


my_set = {"水浒", "西游", "三国"}
print(f"1. my_set:{my_set} 地址是:{id(my_set)}")
f3(my_set)
print(f"4. my_set:{my_set} 地址是:{id(my_set)}")


def f4(my_dict):
    print(f"2.f4() my_dict:{my_dict} 地址是:{id(my_dict)}")
    my_dict['address'] = '兰若寺'
    print(f"3.f4() my_dict:{my_dict} 地址是:{id(my_dict)}")


my_dict = {"name": "小倩", "age": 18}
print(f"1. my_dict:{my_dict} 地址是:{id(my_dict)}")
f4(my_dict)
print(f"4. my_dict:{my_dict} 地址是:{id(my_dict)}")