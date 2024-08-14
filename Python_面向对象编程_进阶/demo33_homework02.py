# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午10:15
# @Note     :   仅作学习使用--禁止传播，违者必究✅

"""
 文件中有Grand,father和son
 问：父类和子类通过self和super（）都可以调用那些属性和方法

"""


class Grand:
    name = 'AA'
    __age = 100

    def g1(self):
        print("Grand-f1()")


class Father(Grand):

    id = '1001'
    __score = None

    def f1(self):
        """
        :return:
        super()可以访问那些成员（属性和方法）？
        答：super().name super().g1()
        self可以访问那些成员 ?
        答：self.id self.__score self.f1() self.g1() self.name

        """
        print("Father-f1()")


class Son(Father):
    name = "BB"

    def g1(self):
        print("Son-g1()")

    def __show(self):
        """
        :return:
        super()可以访问那些成员(属性和方法)？
        答：super().id super().name super().g1() super().f1()
        self可以访问那些成员 ?
        答：self.name self.__show() self.g1() self.id self.f1() self.hi()
        """
        print("Son-show()")

    def hi(self):
        self.__show()


