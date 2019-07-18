

# 方法的重写

class Person:
    def __init__(self, name):
        self.name = name
    def sleep(self):
        print("睡7个小时")

class Man(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def sleep(self):
        print("睡24个小时")

man = Man('老宋')
man.sleep()


