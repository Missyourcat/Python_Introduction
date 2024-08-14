# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午10:26
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 一个养鸡场有6只鸡，它们的体重分别是3kg,5kg,1kg,3.4kg,2kg,50kg.
# 请问这六只鸡的总体重是多少？平均体重是多少？
hen1 = 3
hen2 = 5
hen3 = 1
hen4 = 3.4
hen5 = 2
hen6 = 50
total_weight = hen1 + hen2 + hen3 + hen4 + hen5 + hen6
avg_weight = total_weight / 6
print(f"总体重:{total_weight} 平均体重:{round(avg_weight, 2)}")
# round 保留小数，会四舍五入

# 使用列表解决鸡场问题
hens = [3, 5, 1, 3.4, 2, 50]
total_weight = 0.0
for element in hens:
    total_weight += element
print(f"总体重:{total_weight} 平均体重:{round(total_weight/len(hens), 2)}")
