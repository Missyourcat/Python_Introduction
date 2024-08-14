# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/2 下午4:39
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
定义一个字符串,str_names="tom jack mary noo smith sh",
统计一共多少个人名
如果有"sh"则替换成"申“
如果人名是英文，则把首字母改成大写
"""
str_names = "tom jack mary noo smith sh 张"
print(f"一共{str_names.strip(" ").count(" ") + 1}个人名")
str_names_list = str_names.split(" ")
print(f"一共{len(str_names_list)}个人名")
str_names_replace = str_names.replace("sh", "申")
print(str_names_replace)
"""
 1.定义字符串str_names_upper保存新结果
 2.遍历str_names_list 如果发现是英文名，则将首字母改成大写
 3.拼接到str_names_upper中
 isalpha()判断字符串中的所有字符都为字母并且至少有一个字符则返回True,否则返回false
 capitalize()首字母大写
"""
str_names_upper = ''
for ele in str_names_list:
    if ele.isalpha():
        str_names_upper += ele.capitalize() + "|"
print(str_names_upper)
str_names_upper = str_names_upper.strip("|")
print(str_names_upper)
