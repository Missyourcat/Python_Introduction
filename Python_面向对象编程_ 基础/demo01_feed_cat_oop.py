# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/10 下午11:53
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 定义一个猫类,age,name,color 是属性，或者称为成员变量
# Cat 类
class Cat:
    age = None  # 年龄属性
    name = None  # 名字属性
    color = None  # 颜色属性
    weight = None  # 体重属性


# 通过Cat类，创建 实例(实例对象/对象)
cat01 = Cat()
# 通过对象名.属性名 可以给各个属性赋值
cat01.name = '小白'
cat01.age = 2
cat01.color = '白色'

# 通过对象名.属性名，可以访问到属性
print(f"cat01的信息为: name:{cat01.name} age:{cat01.age} color:{cat01.color}")
