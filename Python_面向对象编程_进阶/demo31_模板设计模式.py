# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午8:06
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import time
from abc import abstractmethod, ABC

"""
1.有多个类，完成不同的任务job
2.要求设计得到各自完成的时间
3.模板设计模式
"""


class Template(ABC):
    @abstractmethod
    def job(self):
        pass

    def cal_time(self):
        start = time.time()
        self.job()
        # 得到结束时间，秒数
        # * 1000变毫秒
        end = time.time()
        print("计算任务 执行时间", (end - start) * 1000)


class AA(Template):
    def job(self):
        num = 0
        for i in range(1, 8000001):
            num += i


class BB(Template):
    def job(self):
        num = 1
        for i in range(1, 8000001):
            num -= i


if __name__ == '__main__':
    aa = AA()
    aa.cal_time()
    bb = BB()
    bb.cal_time()
