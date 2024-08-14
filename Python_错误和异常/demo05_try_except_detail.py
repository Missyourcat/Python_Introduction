# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 下午8:16
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# 如果异常发生了，则异常发生后面的代码不会执行，直接跳入到except子句中
num1 = 10
num2 = 0
try:
    result = num1 / num2
    print("hi")
except Exception as e:
    print(f"出现异常 {e}")
print("继续执行")

# 如果异常没有发生，则顺序执行try的代码块，不会进入到except子句
num1 = 10
num2 = 2
try:
    result = num1 / num2
    print("hi")
except Exception as e:
    print(f"出现异常 {e}")
print("继续执行")

# 如果希望没有发生异常，要执行某段代码，则使用else子句
num1 = 10
num2 = 2
try:
    result = num1 / num2
    print("hi")
except Exception as e:
    print(f"出现异常 {e}")
else:
    # 如果try子句没发生异常，执行else子句
    print("执行了else")
print("继续执行")

# 如果希望不管是否发生异常，都执行某段带按摩(比如关闭连接，释放资源)则使用finally子句
num1 = 10
num2 = 0
try:
    result = num1 / num2
    print("hi")
except Exception as e:
    print(f"出现异常 {e}")
else:
    # 如果try子句没发生异常，执行else子句
    print("执行了else")
finally:
    print("执行了finally")
print("继续执行")

# 可以有多个except子句，捕获不同的异常（进行不同的业务处理），如果发生异常，只会匹配一个except,
# 建议把具体的异常写在前面，基类异常在后比如（IndexError在前，Exception在后），
# 这样当具体异常匹配不到时，再由基类异常匹配
num1 = 10
num2 = 0
try:
    result = num1 / num2
    str_a = 'hello.txt'
    print(str_a[20])
    open('d:/', 'r', encoding='utf-8')
    print("hi")
except IndexError as e:
    print(f"出现异常IndexError {e}")
except ZeroDivisionError as e:
    print(f"出现异常ZeroDivisionError {e}")
except Exception as e:
    print(f"出现异常Exception {e}")
finally:
    print("执行了finally")
print("继续执行")

# 一个except子句，也可以捕获多不同的异常
num1 = 10
num2 = 0
try:
    result = num1 / num2
    str_a = 'hello.txt'
    print(str_a[20])
    open('d:/', 'r', encoding='utf-8')
    print("hi")
except (IndexError, ZeroDivisionError, NameError) as e:
    print(f"出现异常 {e}")
finally:
    print("执行了finally")
print("继续执行")
