# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午8:06
# @Note     :   仅作学习使用--禁止传播，违者必究✅
import time


class AA:
    def job(self):
        # 得到开始的时间，秒数
        start = time.time()
        num = 0
        for i in range(1, 80001):
            num += i
        # 得到结束时间，秒数
        end = time.time()
        print("计算任务 执行时间", (end - start))


class BB:
    def job(self):
        start = time.time()
        num = 1
        for i in range(1, 900):
            num -= i
        end = time.time()
        print("计算任务 执行时间", (end - start))


if __name__ == '__main__':
    aa = AA()
    aa.job()
    bb = BB()
    bb.job()
