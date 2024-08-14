# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 上午12:20
# @Note     :   仅作学习使用--禁止传播，违者必究✅
class Cat:
    age = None        # 年龄属性
    name = "non"  # 名字属性
    color = "红色"  # 颜色属性
    weight = 185.5  # 体重属性


# 通过Cat类，创建 实例(实例对象/对象)
cat01 = Cat()
print(f"cat01的信息为: name:{cat01.name} age:{cat01.age} color:{cat01.color}")
