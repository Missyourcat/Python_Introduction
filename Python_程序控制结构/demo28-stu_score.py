# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/22 下午8:46
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
统计3个班成绩情况，每个班有5名同学，要求完成
1.求出三个班的平均分和所有班级的平均分，学生的成绩从键盘输入
2.统计三个班及格人数
"""
class_num = 3
student_num = 5
sum = 0
count = 0
for i in range(class_num):
    class_sum = 0
    for j in range(student_num):
        score = int(input(f"第{i + 1}个班，第{j + 1}名同学的成绩:"))
        class_sum += score
        if score >= 60:
            count += 1
    sum += class_sum
    print(f"第{i + 1}个班级平均分为{class_sum / student_num}")
print(f"三个班的平均分:{sum / (class_num * student_num)}")
print(f"三个班的合格人数:{count}")
