# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:41
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


obj = BB()
obj2 = AA()
print(f"obj 是不是BB的对象 {isinstance(obj, BB)}")
print(f"obj 是不是AA的对象 {isinstance(obj, AA)}")
print(f"obj 是不是CC的对象 {isinstance(obj, CC)}")
num = 9
print(f"num 是不是int {isinstance(num, int)}")
print(f"num 是不是str {isinstance(num, str)}")
print(f"num 是不是str/int/list:{isinstance(num, (str, int, list))}")
