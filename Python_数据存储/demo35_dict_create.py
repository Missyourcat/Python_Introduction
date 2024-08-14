# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午10:29
# @Note     :   仅作学习使用--禁止传播，违者必究✅
# {字典key的表达式: 字典value的表达式 for 表示key的变量, 表示value的变量 in zip(可迭代对象, 可迭代对象)}
books = ["红楼梦", "三国演义", "西游记", "水浒传"]
authors = ["曹雪芹", "罗贯中", "吴承恩", "施耐庵"]
dict_book = {book: author for book, author in zip(books, authors)}
print(f"{dict_book}")

str_1 = "我爱P"
str_2 = {ele_1: ele_2*2 for ele_1, ele_2 in zip(str_1, str_1)}
print(str_2)

english_list = ["red", "black", "yellow", "white"]
chinese_list = ["红色", "黑色", "黄色", "白色"]
dict_list = {chinese: english.upper() for chinese, english in zip(chinese_list, english_list)}
print(dict_list)
