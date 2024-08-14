# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/13 上午3:53
# @Note     :   仅作学习使用--禁止传播，违者必究✅

# IndexError:当序列抽取超出范围时将被引发，也就是索引错误
str = "hello.txt world"
print(str[100])
list = ['hello.txt', 'world']
print(list[5])

# KeyError:当在现有键集合中找不到指定的映射（字典）键时将被引发
dict = {"id": 1, "name": "tim"}
print(dict["age"])

# NameError:当某个局部或全局名称未找到时将被引发，比如使用一个没有定义的变量名
print("num is", nums)

# TypeError:当一个操作或函数使用了类型不适当的对象时将被引发
a = 'hello.txt'
b = 5
print(a + b)

# ValueError:当操作或函数接收到具有正确类型但值不合适的参数将引发
print(int("123"))
print(int("abc"))

# ZeroDivisionError:当除法或取余运算的第二个参数为0时将被引发
print(1 / 0)

# FileNotFoundError:请求的文件或目录不存在时将被引发
f = open("d://tt", "r")


# AttributeError:当属性引用或赋值失败时将被引发
class A:
    def hi(self):
        pass


a = A()
print(a.name)
