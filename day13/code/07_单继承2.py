

# 父类
class Father(object):
    def __init__(self, name2):
        self.name = name2

# 子类
class Son(Father):
    def __init__(self, name1):
        Father.__init__(self, name1)

    def run(self):
        print("跑步")

# 对象
son = Son("大毛")
print(son.name)
# son.run()

# father
# father = Father('一毛')
# father.run()



# 什么情况下使用继承
#   多个类具有共同属性或方法的情况下
#
# 1，具有从属关系，比如：person -> employee -> manager
#                 比如：ipod  -> ipad  -> iphone
# 2, 两种不同的类具有共同点, 比如：猫Cat和狗Dog都是动物Animal
#                               Animal -> Cat
#                               Animal -> Dog
#




