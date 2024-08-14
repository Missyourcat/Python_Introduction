# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午2:37
# @Note     :   仅作学习使用--禁止传播，违者必究✅

basket = {'apple', 'apple', 'orange', 'pear', 'banana', 'pear'}
# len(集合):集合元素个数
print("basket的元素个数:", len(basket))

# x in s:监测x是否为s中的成员
print("apple" in basket)

# add(element):将元素element添加到集合中
basket.add('grape')
print("basket的元素:", basket)

# remove(element):从集合中移除元素element
# 如果element 不存在于集合中则会引发 keyError
basket.remove('apple')
print("basket的元素:", basket)
# basket.remove('aaa')

# pop():从集合中移除并返回任意一个元素
# 如果集合为空则会引发KeyError
ele = basket.pop()  # 会影响原集合
print("ele:", ele, "类型是:", type(ele))
print("basket的元素:", basket)

# union(*others): 返回一个新集合
# 其中包含来自原集合以及 orthers 指定的所有集合中的元素(并集)
books = {'天龙八部', '笑傲江湖'}
books_2 = {'雪山飞狐', '神雕侠侣', '天龙八部'}
books_3 = books.union(books_2)
print("books_3:", books_3)
books_3 = books | books_2
print("books_3:", books_3)

# intersection(*others): 返回一个新集合
# 其中包含原集合以及 orthers 指定的所有集合中共有的元素(交集)
books_4 = books.intersection(books_2)
print("books_4:", books_4)
books_4 = books & books_2
print("books_4:", books_4)

# difference(*other): 返回一个新集合
# 其中包含原集合以及 orthers 指定的所有集合中不存在的元素(差集)
books_5 = books.difference(books_2)
print("books_5:", books_5)
books_5 = books - books_2
print("books_5:", books_5)
books_6 = books_2 - books
print("books_6:", books_6)
