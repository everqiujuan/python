

class Person:
    def __init__(self, name):
        self.name = name

    # 成员方法
    def run(self):
        print("跑步")

    # 类方法: 可以使用类名来调用，能够使用类属性，但是不能使用对象属性
    #  一般当功能跟类中的其他对象或方法无关时，可以使用类属性，可以一定程度节省内存
    @classmethod
    def eat(cls):
        print(cls == Person)  # True
        p2 = cls('刘翔')

    # 静态方法: 不可以使用对象属性和成员方法，一般也不使用类属性或类方法
    #    就是一个普通的函数，只是写在类中
    @staticmethod
    def sleep():
        print("睡觉")


# 对象
p = Person('苏炳添')
p.run()
# Person.run(p)  # 不建议

p.eat()
Person.eat()  # 推荐

p.sleep()
Person.sleep()

