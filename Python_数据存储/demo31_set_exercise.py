# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午3:00
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
用三个集合表示三门学科的选课学生姓名(一个学生可以同时选多门课)
s_history = {'小明', "张三", '李四', "王五", 'lisa', "Bob"}
s_politic = {'小明', '小花', "小红", "二狗"}
s_english = {'小明', 'lisa', "Bob", "Davil", "李四"}
-求选课学生总共多少人
-求只选了第一个学科的学生数量和学生名字
-求只选了一门学科的学生数量和学生名字
-求选了三门学科的学生数量和学生名字
"""
s_history = {'小明', "张三", '李四', "王五", 'lisa', "Bob"}
s_politic = {'小明', '小花', "小红", "二狗"}
s_english = {'小明', 'lisa', "Bob", "Davil", "李四"}

s_sum = s_history | s_politic | s_english
print(f"总共{len(s_sum)}人")
s_sum = s_history.union(s_politic.union(s_english))
print(f"总共{len(s_sum)}人")

s_history_sum = s_history.difference(s_politic.union(s_english))
print(f"只选了第一个学科的学生有{len(s_history_sum)}人，为{s_history_sum}")
s_history_sum = s_history - s_politic - s_english
# s_history_sum = s_sum - (s_politic | s_english)
print(f"只选了第一个学科的学生有{len(s_history_sum)}人，为{s_history_sum}")

s_history_only = s_history - (s_politic | s_english)
s_politic_only = s_politic - (s_history | s_english)
s_english_only = s_english - (s_history | s_politic)
s_only = s_history_only | s_politic_only | s_english_only
print(f"只选了一门的学生有{len(s_only)}名，为{s_only}")

s_all_sum = s_history.intersection(s_politic.intersection(s_english))
print(f"选了三个班的人有{len(s_all_sum)}个，为{s_all_sum}")
s_all_sum = s_history & s_politic & s_english
print(f"选了三个班的人有{len(s_all_sum)}个，为{s_all_sum}")
