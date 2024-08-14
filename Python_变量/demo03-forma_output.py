# @System   :   Arch Linux
# @Author   :   MR.申
# @File     :   demo03-forma_output.py
# @Time     :   2024/7/3 下午3:11
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 格式化输出案例
name = "tom"
age = 20
score = 99.9
gender = '男'

# %操作符输出 https://blog.csdn.net/hesongzefairy/article/details/104179419
print("个人信息: %s %d %s   %.2f" % (name, age, gender, score))

# format()函数 https://www.runoob.com/python/att-string-format.html
print("个人信息: {}-{}-{}".format(name, age, gender))

# f-strings https://blog.csdn.net/weixin_44200553/article/details/130408971
print(f"个人信息: {name} {age} {gender} {score}")
