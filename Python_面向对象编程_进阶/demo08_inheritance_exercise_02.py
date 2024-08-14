# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午11:43
# @Note     :   仅作学习使用--禁止传播，违者必究✅
"""
编写Computer类，包含CPU,内存，硬盘等属性
1.get_details方法用于返回Computer的详细信息
2.编写PC子类，继承Computer类，添加特有属性【品牌brand】
3.编写NotePad子类，继承Computer类，添加特有属性[color]
4.完成测试，创建PC和NotePad对象，分别给对象中贴有的属性赋值，以及从Computer类继承的属性赋值，并使用方法打印细信息
"""


class Computer:
    CPU = None
    Memory = None
    disk = None

    def __init__(self, CPU, Memory, disk):
        self.CPU = CPU
        self.Memory = Memory
        self.disk = disk

    def get_details(self):
        return f"CPU:{self.CPU} Memory:{self.Memory} disk:{self.disk}"


class PC(Computer):
    brand = None

    def __init__(self, CPU, Memory, disk, brand):
        """
        1.通过super().xx 方式可以去调用父类的方法
        2.调用父类属性的构造方法完成对父类属性的初始化任务
        3.self.brand = brand 表示子类特有的属性又子类完成

        """
        super().__init__(CPU, Memory, disk)
        self.brand = brand

    def info(self):
        print(f"{self.get_details()} brand:{self.brand}")


class NotePad(Computer):
    color = None

    def __init__(self, CPU, Memory, disk, color):
        super().__init__(CPU, Memory, disk)
        self.color = color

    def info(self):
        print(f"{self.get_details()} color:{self.color}")


pc = PC("i5", "512MB", "fdisk", 'amd')
pc.info()
notepad = NotePad("A15", "1G", "mac", "black")
notepad.info()
