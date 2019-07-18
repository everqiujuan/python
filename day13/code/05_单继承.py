


# 继承

# 人类
# class Person:
#    def __init__(self):
#       name, age, sex, height, weight, hair, qq, wechat
#
# 男人类 （男人累）
# class Man:
#    def __init__(self):
#       name, age, sex, height, weight, hair, qq, wechat, huzi, houjie
#
# 女人类（女人泪）
# class Female:
#   def __init__(self):
#       name, age, sex, height, weight, hair, qq, wechat，longhair
#
#
# 使用继承
# 人类
# class Person:
#    def __init__(self):
#       name, age, sex, height, weight, hair, qq, wechat
#    def sleep(self):
#       print('')
#
# 男人类
# class Man(Person):
#    def __init__(self):
#       huzi, houjie
#    def sleep(self):
#        print('边打鼾边睡觉')
# 女人类
# class Female(Person):
#   def __init__(self):
#       longhair
#    def sleep(self):
#        print('边磨牙边睡觉')


# 面向对象的特点：封装，继承，多态
#   封装：类把属性(变量)和方法(函数)封装在类的内部
#   继承：子类可以继承父类的属性和方法，也可以扩展自己的属性或方法
#   多态：在继承的基础上，可以通过父类对象指向不同的子类对象，调用相同名称的方法可以有不同的状态


# 继承
# 单继承：只有一个父类
#   多重继承： 多重的单继承
# 多继承：有多个父类

# 单继承
# 父类
class Ipod(object):
    def __init__(self, color):
        self.color = color
    def listen_music(self):
        print("听音乐")

# 子类
class Ipad(Ipod):
    def __init__(self, color, size):
        # 调用父类的init方法
        # Ipod.__init__(self, color)  # 显式调用
        super().__init__(color)  # 隐式调用 简写
        # super(Ipad, self).__init__(color)  # 隐式调用 老版本

        self.size = size

    def watch_movie(self):
        print("看生化危机")


# 子类对象
ipadmini = Ipad('土豪金', '7.9寸')
print(ipadmini.color)
print(ipadmini.size)
ipadmini.listen_music()
ipadmini.watch_movie()



