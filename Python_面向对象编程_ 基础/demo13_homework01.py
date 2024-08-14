# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 定义类A01,定义方法max,实现求某个float列表list=[1.1, 2.9, -1.9, 67.9]的最大值，并返回
# class A01:
#     my_list = None
#
#     def max(self):
#         return max(self.my_list)
#
#
# list = A01()
# list.my_list = [1.1, 2.9, -1.9, 67.9]
# print(list.max())

class A01:
    def max(self, lst):
        return max(lst)


a = A01()
print(a.max([1.1, 2.9, -1.9, 67.9]))
