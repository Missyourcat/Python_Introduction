# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/16 下午4:07
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 赋值运算法
num1 = 10
i = 100
i += 100
print("i=", i)
i -= 100
print("i=%d" % i)
i *= 3
print(f"i={i}")

# a和b进行交换
a = 30
b = 40
"""
1.定义中间temp
2.把a的值保存到temp
3.把b的值赋给a
4.把temp值给b
"""
print(f"没有交换前, a={a}, b={b}")
temp = a
a = b
b = temp
print(f"交换后, a={a}, b={b}")

"""
在python中支持一个简单非的方式实现变量交换
x, y = y, x
"""
a, b = b, a
print(f"交换后, a={a}, b={b}")

