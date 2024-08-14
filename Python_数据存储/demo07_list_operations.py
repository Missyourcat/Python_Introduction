# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/29 下午1:41
# @Note     :   仅作学习使用--禁止传播，违者必究✅

list_a = [100, 200, 300, 400, 600]
print("list_a 列表元素个数:", len(list_a))
print("list_a 列表最大元素:", max(list_a))
print("list_a 列表最小元素:", min(list_a))

list_a.append(900)
print("list_a:", list_a)

print("100出现的次数:", list_a.count(100))

list_b = [1, 2, 3]
list_a.extend(list_b)
print("list_a:", list_a)

print("300第1次出现在序列的索引是:", list_a.index(300))

list_a.reverse()
print("翻转后的list:", list_a)

list_a.insert(1, 666)  # 把666插入到索引为1的位置
print("list_a:", list_a)
