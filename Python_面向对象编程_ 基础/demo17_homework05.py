# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/11 下午1:56
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 定义Music类，里面有音乐name,音乐时长times属性，并有播放play功能，和返回本身属性信息的方法get_info
class Music:
    def __init__(self, name, times):
        self.name = name
        self.times = times

    def play(self):
        print(f"{self.name}正在播放，时间是:{self.times}")

    def get_info(self):
        return f"音乐的信息:{self.name},时长:{self.times}"


m1 = Music("qq", 3)
m2 = Music("wx", 4)
m1.play()
m2.play()
print(m1.get_info())