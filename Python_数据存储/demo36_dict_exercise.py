# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/8 下午10:43
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
一个公司有多个员工，请使用适合的数据类型保存员工的信息(比如员工号，年龄，名字，入职时间，薪水)
1)员工号是入职时分配的，唯一不重复
2)同员工号，可以查询员工的信息
3)可以根据需要，可以动态的增加，删除员工
4)可以根据需要，可以修改员工信息
5)遍历所有员工，把所有员工的薪水，在原工资的基础上，增加20%
6)按规定格式输出
"""
clerks = {
    "0001": {
        "age": 20,
        "name": "贾宝玉",
        "entry_time": "2011-11-11",
        "sal": 12000
    },
    "0002": {
        "age": 21,
        "name": "薛宝钗",
        "entry_time": "2015-12-12",
        "sal": 10000
    },
    "0003": {
        "age": 18,
        "name": "林黛玉",
        "entry_time": "2018-10-10",
        "sal": 10086
    }
}

print(f"员工号为0003的信息为 名字:{clerks['0003']['name']} 年龄:{clerks['0003']['age']} "
      f"入职时间:{clerks['0003']['entry_time']} 薪水:{clerks['0003']['sal']}")

clerks['0004'] = {
    "age": 30,
    "name": "BRO",
    "entry_time": "2024-9-1",
    "sal": 10
}
print(clerks)
# del clerks['0001']
clerks.pop('0001')
print(clerks)

clerks['0004']['name'] = 'ok'
clerks['0004']['age'] = 20
clerks['0004']['sal'] += clerks['0004']['sal'] * 0.1
print(f"员工号为0004的信息为 名字:{clerks['0004']['name']} 年龄:{clerks['0004']['age']} "
      f"入职时间:{clerks['0004']['entry_time']} 薪水:{clerks['0004']['sal']}")

keys = clerks.keys()
for element in keys:
    clerks[element]['sal'] *= 1.2
for ele in keys:
    print(f"员工号为{ele}的信息为 名字:{clerks[ele]['name']} 年龄:{clerks[ele]['age']} "
          f"入职时间:{clerks[ele]['entry_time']} 薪水:{clerks[ele]['sal']}")
for ele in keys:
    clerk_info = clerks[ele]
    print(f"员工号为{ele}的信息为 名字:{clerk_info['name']} 年龄:{clerk_info['age']} "
          f"入职时间:{clerk_info['entry_time']} 薪水:{round(clerk_info['sal'], 2)}")
