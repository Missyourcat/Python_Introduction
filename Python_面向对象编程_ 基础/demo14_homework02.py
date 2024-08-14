# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 编写类Book,定义方法update_price,实现更改某本书的价格
"""
如果价格>150,则更改为150
如果价格>100,更改为100
否则不变
"""


class Book:
    name = None
    price = None

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def update_price(self):
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100
        else:
            pass

    def info(self):
        print(f"{self.name} {self.price}")


book1 = Book("红楼梦", 20)
book2 = Book("红楼梦1", 120)
book3 = Book("红楼梦2", 150)
book4 = Book("红楼梦3", 170)
book1.update_price()
print(f"{book1.name} {book1.price}")
book2.update_price()
print(f"{book2.name} {book2.price}")
book3.update_price()
print(f"{book3.name} {book3.price}")
book4.update_price()
print(f"{book4.name} {book4.price}")
