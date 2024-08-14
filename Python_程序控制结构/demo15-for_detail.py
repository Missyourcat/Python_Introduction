# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 上午12:01
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
range函数的解读
class range(stop)
class range(start, stop, step=1)
1.虽然被称为函数,但range实际上是一个不可变的序列类型
2.range默认增长的步长step是1,也可以指定，start默认是0
3.通过list（）可以看range（）生成的序列包含的数据
4.range（）生成的数列是前闭后开
"""
# 生成[1,2,3,4,5]
r1 = range(1, 6, 1)
print(list(r1))
# 生成[0,1,2,3,4,5]
r2 = range(6)
print(list(r2))
# 生成[1,3,,5,7,9]
r3 = range(1, 10, 2)
print(list(r3))
# for+range输出10句话
for i in range(1, 11):
    print("hello.txt,python", i)
