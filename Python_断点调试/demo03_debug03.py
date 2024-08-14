# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/9 下午11:10
# @Note     :   仅作学习使用--禁止传播，违者必究✅

def f2(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res


def f1(name):
    print(f"name={name} 1")
    print(f"name={name} 2")
    print(f"name={name} 3")
    print(f"name={name} 4")
    print(f"name={name} 5")
    r = f2(6)
    print(f"r={r}")
    print(f"name={name} 6")
    print(f"name={name} 7")
    print(f"name={name} 8")


f1("python")
print("end...")
