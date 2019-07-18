

# 面向对象：
#   封装：用类把属性和方法封装起来
#   继承：子类可以继承父类的属性和方法，也可以扩展自己独有的属性或方法
#   多态：在继承的基础上，不同的子类重写父类的同一个方法，父类对象可以指向不同的子类对象，
#        调用重写的方法，会有不同的效果

# 动物
class Animal:
    def beat(self):
        pass

# 狗
class Dog(Animal):
    def beat(self):
        print("汪汪的叫~~然后咬你一口")

# 猫
class Cat(Animal):
    def beat(self):
        print("喵喵的叫~~然后抓你一把")

# 狼
class Wolf(Animal):
    def beat(self):
        print("嗷嗷的叫~~然后吃了你")

# 类
class Person:
    def __init__(self, name):
        self.name = name
    def beat_animal(self, animal):
        print(self.name, "正在殴打小动物")
        animal.beat()

dog = Dog()
cat = Cat()
wolf = Wolf()

xiaoming = Person("黄晓明")
xiaoming.beat_animal(wolf)
