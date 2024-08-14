# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/2 下午3:41
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
定义一个元组，('大话西游', '周星驰', 80, ['周星驰', '小甜甜']),信息为
(1)查询票价对应的索引
(2)遍历所有的演员
(3)删除‘小甜甜’，增加 演员‘牛魔王’，‘猪八戒’
"""
tuple_movie = ('大话西游', '周星驰', 80, ['周星驰', '小甜甜'])
print("票价对应的索引:", tuple_movie.index(80))
for ele in tuple_movie[3]:
    print("演员的名字:", ele)
print("------------------------------------")
del tuple_movie[3][1]
tuple_movie[3].append("牛魔王")
tuple_movie[3].append("猪八戒")
for ele in tuple_movie[3]:
    print("演员的名字:", ele)
print("------------------------------------")
new_actor = ["白晶晶", "紫霞仙子"]
tuple_movie[3].extend(new_actor)
for ele in tuple_movie[3]:
    print("演员的名字:", ele)
