# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午12:33
# @Note     :   仅作学习使用--禁止传播，违者必究✅
print("---下面对象的布尔值为False---")
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(set()))

# 因为所有对象都有一个布尔值，所以有些代码直接使用对象的布尔值做判断
content = 'hello.txt'
print(bool(content))
content = ""
if content:
    print(f"hi {content}")
else:
    print("空字符")

lst = [1, 2]
if lst:
    print(f"lst: {lst}")
else:
    print("空列表")