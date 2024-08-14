# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:55
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
1.定义员工类Employee ,包含私有属性(姓名和月工资)，以及计算年工资get_annual的方法
2.普通员工(Worker)和经理(Manager)继承员工类，经理类多了奖金bonus属性和管理manage方法，
普通员工类多了work方法，普通员工和经理类要求根据需要重写get_annual方法
3.编写函数show_emp_annual(e:Employee),实现获取任何员工对象的年工资
4.编写函数working(e:Employee),如果是普通员工，则调用work方法，如果是经理，则调用manage方法
"""


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_annual(self):
        return self.__salary * 12

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary


class Worker(Employee):
    def work(self):
        print(f"员工{self.get_name()}在工作")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.__bonus = bonus

    def manage(self):
        print(f"经理{super().get_name()}在管理")

    def get_annual(self):
        return super().get_annual() + self.__bonus


def show_emp_annual(e: Employee):
    print(f"{e.get_name()}的年工资是{e.get_annual()}")


def working(e: Employee):
    if isinstance(e, Worker):
        e.work()
    elif isinstance(e, Manager):
        e.manage()
    else:
        pass


work = Worker("小明", 20000)
manager = Manager("王总", 40000, 2000)
show_emp_annual(work)
show_emp_annual(manager)
working(work)
working(manager)
