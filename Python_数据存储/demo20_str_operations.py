# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/2 下午4:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅

str_names = "jack tom mary ok noo tom"
print(f"{str_names}有{len(str_names)}个字符")

"""
 str.replace(old, new[, count]):
 返回字符串的副本，其中出现的所有子字符串 old 都将被替换为 new
 如果给出了可选参数count,则只替换前count次出现
 返回字符串的副本 表示原来的字符串不变，而是返回一个新的字符串
"""
str_names_new = str_names.replace("jack", "杰克", 1)
print("str_names_new:", str_names_new, id(str_names_new))
print("str_names:", str_names, id(str_names))

"""
 str.split(sep=None, maxsplit=- 1):
 返回一个由字符串内单词组成的列表，使用sep作为分隔字符串
 如果给出了maxsplit,则最多进行maxsplit次拆分(因此，列表最多会有maxsplit + 1个元素)
 如果maxsplit未指定或为-1,则不限制拆分次数(进行所有可能拆分)
"""
str_names_split = str_names.split(" ", 2)
print(f"str_names_split 内容是 {str_names_split} 类型:{type(str_names_split)}")
print(f"str_names:{str_names}")

# str.count(sub):统计指定字符串在字符串中出现的次数
print("tom在字符串中出现的次数:", str_names.count("tom"))
print(f"tom出现的索引：{str_names.index("tom")}")

"""
 str.strip([chars]):
 返回原字符串的副本，移除其中的前导和末尾字符。
 chars为指定要移除字符的字符串
 通常用于除去前后的空格，或者去掉指定的某些字符
"""
str_names_strip = str_names.strip(" ")
print(" jack ".strip(" "))
print("123jack321".strip("213"))  # 很6的操作

"""
 str.lower():
 返回原字符串小写的副本，不影响原来的字符串
 str.upper():
 返回原字符串大写的副本，不影响原来的字符串
"""
str_names = "Python"
str_names_lower = str_names.lower()
print("str_names_lower:", str_names_lower)
print("str_names:", str_names)
str_names_upper = str_names.upper()
print("str_names_upper:", str_names_upper)
print("str_names:", str_names)
