# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午2:23
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 集合是由不重复元素组成的无序容器
# 不重复元素组成，可以理解成会自动去重
basket = {'apple', 'apple', 'orange', 'pear', 'banana', 'pear'}
print(f"basket: {basket}")

# 无序，也就是你定义元素的顺序和取出的顺序不能保持一致
# 集合底层会按照自己的一套算法来存储和取数据，所以每次取出的顺序是不变的
set_a = {100, 200, 300, 400, 500}
print(f"set_a:{set_a}")
print(f"set_a:{set_a}")
print(f"set_a:{set_a}")

# 集合不支持索引
# print(set_a[2])

# 使用for循环对集合进行遍历
print("-" * 30)
for element in basket:
    print(element)

# 创建空集合只能用set(),不能用{}(空字典)
set_b = {}
set_c = set()
print(f"set_b:{set_b} 类型:{type(set_b)} set_c:{set_c} 类型:{type(set_c)}")
