# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/29 下午1:09
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 空列表可以通过[],或者list()方式来定义
list1 = []
list2 = list()
print(list1, type(list1))
print(list2, type(list2))

# 列表元素可以有多个，而且数据类型没有限制，允许有重复元素，并且是有序的
list3 = [100, 'jack', 4.5, True, 'jack']
print(list3)
# 嵌套列表
list4 = [100, 'tom', ["天龙八部", "笑傲江湖", 300]]
print("list4=", list4)

# 列表的索引/下标是从0开始的

# 列表索引必须在指定范围内使用，否则报错
list5 = [1, 2.1, "我爱python"]
# print(list5[3])  # 越界索引

# 索引也可以从尾部开始，最后一个元素的索引为-1,往前一位为-2
list5_back = [1, 2.1, "我爱python"]
print(list5_back[-1])
print(list5_back[-2])
# 不能越界
# print(list5_back[-4])

# 通过 列表[索引]=新值 对数据进行更新，使用 列表.append(值)方法来添加元素，使用del语句来删除列表的元素，注意不能超出有效索引范围
list_a = ["天龙八部", "笑傲江湖"]
print("list_a=", list_a)
list_a[0] = "雪山飞狐"
print("list_a=", list_a)
list_a.append("倚天屠龙")
print("list_a=", list_a)
del list_a[1]
print("list_a=", list_a)

# 列表是可变序列
list6 = [1, 2.1, '我爱python']
print(f"list:{list6},地址:{id(list6[1])},{id(list6[2])},{id(list6)}")
list6[2] = 'lalala'
print(f"list:{list6},地址:{id(list6[1])},{id(list6[2])},{id(list6)}")

# 列表赋值特点
list7 = [1, 2.1, '我爱python']
list8 = list7
list8[0] = 500
print("list7=", list7)
print("list8=", list8)


# 列表传参特点


def f1(l):
    l[0] = 100
    print("l的id:", id(l))


list9 = [1, 2.1, 200]
print("list9的id:", id(list9))
f1(list9)
print("list9:", list9)
