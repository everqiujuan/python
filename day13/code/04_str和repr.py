

# __str__()
# __repr__()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 输出对象时会自动调用__str__方法，并返回内容
    def __str__(self):
        return "姓名1：%s，年龄：%d" % (self.name, self.age)

    # def __repr__(self):
    #     return "姓名2：%s，年龄：%d" % (self.name, self.age)

# 对象
p = Person("小黄", 33)
# print(p)  # <__main__.Person object at 0x00000000021E9E80>
print(p)  # '姓名：小黄，年龄：33'
# print(repr(p))



