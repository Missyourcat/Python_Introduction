# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/13 下午10:27
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 显式类型转换注意事项
# 不管什么值的int,float都可以转换成str
n1 = 100
n2 = 123.41
print(str(n1))
print(str(n2))

# int转换成float时，会增加小数部分
# float转换成int时，会去掉小数部分
print(float(n1))
print(int(n2))

# str转int,float使用int(x),float(x)将对象x转换成int/float
n3 = "12.3"
print(float(n3))
# print(int(n3))

n4 = "hello.txt"
# print(float(n4))
# print(int(n4))

i = 10
j = float(i)
print("i的值:", i, "i的类型:", type(i))
print("j的值:", j, "j的类型:", type(j))
k = str(i)
print("i的值:", i, "i的类型:", type(i))
print("k的值:", k, "k的类型:", type(k))
