

# 父类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性，只能在当前类内部使用

    def fn(self):
        print("fn")
        self.__fn2()
        return self.__age

    def __fn2(self):  # 私有方法，只能在当前类内部使用
        print("__fn2")

# p = Person('小头爸爸', 30)
# print(p.name)
# print(p.age)
# p.fn()
# p.__fn2()

# 子类
class Man(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
    def fn3(self):
        print(self.fn())

# man对象
man = Man('老王', 60)
# print(man.name)
# print(man.age)  # 私有属性不能被继承
# man.fn()
# man.fn2()  # 私有方法不能被继承
man.fn3()

