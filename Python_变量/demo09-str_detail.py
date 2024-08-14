# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/6 下午4:19
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 使用引号( ' 或 " )包裹起来，创建字符串
str1 = 'tom说:"hello.txt"'
print(str1)
str2 = "jack说:'hi'"
print(str2)

print(f"str2的类型：{type(str2)}")

# 通过加号可以连接字符串
print("hi" + " tom")

# python 不支持单字符类型，单字符在python中作为一个字符串使用
str3 = 'A'
print("str3类型", type(str3))

# 用三个单引号'''内容'''，或用三个双引号"""内容"""可以使字符串内容保持原样输出，在输出格式复杂的内容是比较有用的

content = """
/home/Missyourcat/learn/Python_code/pythonProject/venv/bin/python
/home/Missyourcat/learn/Python_code/pythonProject/Python_变量/demo09-str_detail.py 
tom说:"hello.txt"
jack说:'hi'
str2的类型：<class 'str'>
hi tom
str3类型 <class 'str'>
"""
print(content)

# 在字符串前面加'r' 可以使整个字符串不被转义
str4 = r"jack\ntom\tking"
print(str4)

# 字符串驻留机制
str1 = "hello.txt"
str2 = "hello.txt"
str3 = "hello.txt"

# id()函数，可以返回对象的“标识值”，对象/数据的内存地址
print("str1的地址:", id(str1))
print("str2的地址:", id(str2))
print("str3的地址:", id(str3))

"""
驻留机制几种情况讨论
(1)字符串是由26个英文字母大小写，0-9,_组成
(2)字符串长度为0或者1
(3)字符串在编译时进行驻留，而非运行
(4)【-5,256】的整数数字
"""
a = "abcABC_123"
b = "abcABC_123"
print("a的地址:", id(a))
print("b的地址:", id(b))
a = "abcABC_123#"
b = "abcABC_123#"
print("a的地址:", id(a))
print("b的地址:", id(b))
a = ""                 
b = ""                 
print("a的地址:", id(a))   
print("b的地址:", id(b))   
a = "#"
b = "#"
print("a的地址:", id(a))
print("b的地址:", id(b))
a = "abc"
b = "".join(["a", "bc"])
print("a的地址:", id(a), a)
print("b的地址:", id(b), b)
a = -6                 
b = -6                 
print("a的地址:", id(a))   
print("b的地址:", id(b))
a = 289
b = 289
print("a的地址:", id(a))   
print("b的地址:", id(b))
# Pycharm进行了优化，原生会出现差异
