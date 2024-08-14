# @System   :   Arch Linux
# @Author   :   MR.申
# @Time     :   2024/8/12 下午3:18
# @Note     :   仅作学习使用--禁止传播，违者必究✅

class Food:
    def __init__(self, name):
        self.name = name


class Fish(Food):
    pass


class Bone(Food):
    pass


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Horse(Animal):
    pass


class Grass(Animal):
    pass


class Master:
    def __init__(self, name):
        self.name = name

    def feed(self, animal: Animal, food: Food):
        print(f"主人 {self.name} 给动物:{animal.name} 喂的食物是:{food.name}")


master = Master("ok")
cat = Cat("汤姆")
fish = Fish("小鲤鱼")
dog = Dog("实派克")
bone = Bone("大鼓棒")
horse = Horse("马")
grass = Grass("草")

master.feed(cat, fish)
master.feed(horse, grass)
master.feed(dog, bone)
