# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午8:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 字典的Key（关键值）通常是字符串或数字，Value可以是任意数据类型
dict_a = {
    'list': [100, 200, 300],
    "tuple": (10, 20, "hello.txt"),
    "set": {"apple", 'pear'},
    "str": "python课",
    "dict字典": {
        "性别": "男",
        "age": 18,
        "地址": "香港"
    },
    'key1': 100,
    'key2': True
}
print(f"dict_a:{dict_a} 类型:{type(dict_a)}")
print(f"dict_a:{dict_a["list"]} 类型:{type(dict_a["list"])}")
print(f"dict_a:{dict_a["tuple"]} 类型:{type(dict_a["tuple"])}")
print(f"dict_a:{dict_a["set"]} 类型:{type(dict_a["set"])}")

# 字典不支持索引
# print(dict_a[0])

# 既然字典不支持索引，所以对字典进行遍历不支持while,只支持for,注意直接对字典进行遍历，遍历得到是Key
dict_b = {'one': 1, 'two': 2, "three": 3}
# 依次取出key,再通过dict[key]取出对应的value
print("-----------遍历方式1--------------")
for key in dict_b:
    print(f"key: {key} value: {dict_b[key]}")
# 依次取出value
print("-----------遍历方式2--------------")
for value in dict_b.values():
    print(f"value: {value}")
# 依次取出key-value
print("-----------遍历方式3--------------")
for k, v in dict_b.items():
    print(f"key:{k} value:{v}")

# 创建空字典可以通过{},或者dict()
dict_c = {}
dict_d = dict()
print(f"dict_c:{dict_c} 类型：{type(dict_c)}")
print(f"dict_c:{dict_d} 类型：{type(dict_d)}")

# 字典的key必须是唯一的，如果指定多个相同的key,后面的键值对会覆盖前面的
dict_e = {'one': 1, 'two': 2, 'three': 3, "two": 200}
print("dict_e", dict_e)
