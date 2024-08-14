# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/7/23 下午4:58
# @Note     :   仅作学习使用--禁止传播，违者必究✅

def f1(a):
    print(f"f1() a的值:{a} 地址是:{id(a)}")
    a += 1
    print(f"f1() a的值:{a} 地址是:{id(a)}")


a = 10
print(f"调用前f1() a的值:{a} 地址是:{id(a)}")
f1(a)
print(f"调用后f1() a的值:{a} 地址是:{id(a)}")


def f2(name):
    print(f"f2() name的值:{name} 地址是{id(name)}")
    name += " hi"
    print(f"f2() name的值:{name} 地址是{id(name)}")


print("------------------")
name = "tome"
print(f"调用前f2() name的值:{name} 地址是{id(name)}")
f2(name)
print(f"调用后f2() name的值:{name} 地址是{id(name)}")
