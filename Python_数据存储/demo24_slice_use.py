# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/2 下午4:57
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 切片操作前闭后开
str = "hello.txt,world"
str_slice = str[0:5:1]
print("str_slice:", str_slice)

list_a = ["jack", "tom", "yoyo", "python"]
list_slice = list_a[1:5:2]
print("list_slice:", list_slice)

tuple_a = (100, 200, 300, 400, 500)
tuple_slice = tuple_a[1:5:1]
print("tuple_slice:", tuple_slice)
