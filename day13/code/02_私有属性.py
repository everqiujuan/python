
# 私有属性

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self._age = age

        # 私有属性：给普通属性前添加两个下划线__sex,则该属性会变成私有属性
        #    特点：只能在当前类内部使用，子类不能继承父类的私有属性
        self.__sex = sex

    def sleep(self):
        print("睡觉", self.__sex)

    # 间接访问
    # get或set
    def getSex(self):
        return self.__sex
    def setSex(self, sex):
        if sex in ['男', '女']:
            self.__sex = sex


# 对象
p = Person("旺财", 2, '男')
print(p.name)
print(p._age)
# print(p.sex)  # 报错
# print(p.__sex)  # 报错
# p.sleep()

# 间接访问私有属性
print(p.getSex())  # 男
p.setSex('女')
print(p.getSex())  # 女

# _类名__私有属性： 可以直接访问私有属性，不推荐使用
print(p._Person__sex)  # 女
p._Person__sex = '人妖'
print(p._Person__sex)  # 人妖


#
# name, age, sex: 普通变量，普通属性
# __sex : 私有属性
# _age : 普通变量或属性，不建议这么用，如果要使用单个下划线，
#       则你要认为这就是一个私有属性，不要类外使用它
# __name__ : 特殊变量
#




