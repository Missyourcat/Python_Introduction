# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/2 下午3:36
# @Note     :   仅作学习使用--禁止传播，违者必究✅

tuple_a = (100, 200, 300, 400, 200, 100)
print("tuple_a 元组元素个数", len(tuple_a))
print("tuple_a 元组最大元素", max(tuple_a))
print("tuple_a 元组最小元素", min(tuple_a))
print("100出现的次数:", tuple_a.count(100))
print("200出现的次数:", tuple_a.count(200))
print("200第一次出现的索引是:", tuple_a.index(200))
print("300是否在元组中存在:", 300 in tuple_a)