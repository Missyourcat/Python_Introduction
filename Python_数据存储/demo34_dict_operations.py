# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午9:44
# @Note     :   仅作学习使用--禁止传播，违者必究✅

dict_a = {'one': 1, 'two': 2, "three": 3}

print(f"dict_a 的元素个数是:{len(dict_a)}")

# d[key]: 返回d中以key为键的项。如果映射中不存在key则会引发KeyError
print("key为three对应的value:", dict_a['three'])
# print("key为three对应的value:", dict_a['three1'])

"""
 d[key] = value: 将d[key]设为value,如果key已经存在, 则是修改value,
 如果key没有存在，则是增加key-value,注意会直接修改原来的字典
"""
dict_a['one'] = '第一'
print(f"dict_a:{dict_a}")
# 增加key为'four' value为4
dict_a['four'] = 4
print(f"dict_a:{dict_a}")

# del d[key]:将d[key]从d中移除。如果映射中不存在key则会引发KeyError
del dict_a['four']
print(f"dict_a:{dict_a}")

"""
 pop(key[, default]):
 如果key存在于字典中则将其移除并返回其值，否则返回default
 如果default未给出且key不存在字典中，则会引发KeyError
"""
val = dict_a.pop('one')
print(f"val:{val}")
print(f"dict_a:{dict_a}")
val = dict_a.pop('one_', 'haha')
print(f"val:{val}")
print(f"dict_a:{dict_a}")

# keys():返回字典所有的key
dict_a_keys = dict_a.keys()
print(f"dict_a_keys:{dict_a_keys} 类型{type(dict_a_keys)}")
for k in dict_a_keys:
    print("k->", k)

# key in d:如果d中存在键key则返回True,否则返回False
print("two" in dict_a)

# clear():移除字典中的所有元素
dict_a.clear()
print("dict_a", dict_a)
