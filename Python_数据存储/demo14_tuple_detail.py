# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/1 下午12:20
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 空元组可以通过()或者tuple()来定义
tuple_a = ()
tuple_b = tuple()
print(f"tuple_a 内容是{tuple_a} 类型是{type(tuple_a)}")
print(f"tuple_b 内容是{tuple_b} 类型是{type(tuple_b)}")

# 元组的元素有多个，而且数据类型没有限制( 可以嵌套元组 ），允许有重复元素，并且是有序的
tuple_c = (100, 'jack', 4.5, True, "jack")
print(tuple_c)
tuple_d = (100, "tom", ("天龙八部", "笑傲江湖", 300))
print("tuple_d=", tuple_d)

# 元组的索引/下标是从0开始的

# 元组索引必须在指定范围内使用，否则报错
tuple_e = (1, 2.1, "我爱python")
# print(tuple_e[3])

# 元组是不可变序列
tuple_f = (1, 2.1, "我爱python")
# tuple_f[2] = '222'  # 不可变序列

# 可以修改元组内list的内容(包括 增删改 等)
tuple_g = (1, 2.1, "我爱python", ["jack", "tom", "mary"])
print(tuple_g[3])
print(tuple_g[3][0])
# 修改
tuple_g[3][0] = "hsp"
print(tuple_g)
# 删除
del tuple_g[3][0]
print(tuple_g)
# 增加
tuple_g[3].append("ok")
print(tuple_g)

# 索引也可以从尾部开始，最后一个元素的索引为-1,前一位为-2
tuple_h = (1, 2.1, "我爱python", ["jack", "tom", "mary"])
print(tuple_h[-2])

# 定义只有一个元素的元组，需要带上逗号，否则不是元组类型
tuple_i_1 = (100)
tuple_i_2 = (100,)
tuple_i_3 = (100, 200)
print(f"tuple_i_1类型:{type(tuple_i_1)}")
print(f"tuple_i_2类型:{type(tuple_i_2)}")
print(f"tuple_i_3类型:{type(tuple_i_3)}")
