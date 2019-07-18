
# 单继承： 只有一个父类
# 多继承： 有多个父类

# Father
class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print("会工作赚钱")

# Mother
class Mother(object):
    def __init__(self, facevalue, height):
        self.facevalue = facevalue
        self.height = height
    def shopping(self):
        print("会购物")
# Son
class Son(Father, Mother):
    def __init__(self, name, age, facevalue, height, girl_friend):
        # 显示调用继承
        Father.__init__(self, name, age)  # 调用Father的init方法
        Mother.__init__(self, facevalue, height)  # 调用Mother的init方法

        # 隐式调用继承
        # super().__init__(name, age)  # 调用Fahter的init
        # super(Son, self).__init__(name, age)  # 调用Fahter的init
        # super(Father, self).__init__(facevalue, height)  # 调用Mother的init
        # 从左往右依次继承Fahter和Mother，内部有mro的算法

        self.girl_friend = girl_friend
    # 泡妞
    def chasingGril(self):
        print("会泡妞")

# son对象
son = Son('大头儿子', 6, 100, 1, '棉花糖')
print(son.name, son.age, son.facevalue, son.height)
son.work()
son.shopping()

print(son.girl_friend)
son.chasingGril()
