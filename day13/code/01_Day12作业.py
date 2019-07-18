
# 利用面向对象的思想写下面的程序
# 1.小美在朝阳公园溜旺财【注：旺财是狗】
class Person:
    def __init__(self, _name):
        self.name = _name
    def play_dog(self, dog):
        print("%s在朝阳公园溜%s" % (self.name, dog))

xiaomei = Person("小美")
xiaomei.play_dog('旺财')


# 2.小明穿着白色的特步运动鞋在奥林匹克公园跑步
class Person2:
    def __init__(self, name, shoes):
        self.name = name
        self.shoes = shoes
    def run(self, place):
        print("%s穿着%s在%s跑步" % (self.name, self.shoes, place))

xiaoming = Person2("小明", '白色的特步运动鞋')
xiaoming.run("奥林匹克公园")


# 3.赵老师在讲台上讲课，小刚认真的听课做笔记
class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self):
        print("%s在讲台上讲课" % self.name)

class Student:
    def __init__(self, name):
        self.name = name
    def listen(self, teacher):
        print("%s认真的听%s的课做笔记" % (self.name, teacher.name))

teacher_zhao = Teacher("赵老师")
xiaogang = Student("小刚")
teacher_zhao.teach()
xiaogang.listen(teacher_zhao)
print(teacher_zhao)


# 4.张阿姨和李阿姨在物美超市买红富士
class Aunt:
    def __init__(self, name):
        self.name = name
    def buy(self, goods):
        print("%s在物美超市买%s" % (self.name, goods))

aunt_zhang = Aunt('张阿姨')
aunt_li = Aunt('李阿姨')
aunt_zhang.buy("红富士")
aunt_li.buy("红富士")


# 使用构造函数的方式写下面的程序
# 1.定义一“圆”（Circle）类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, r, center):
        self.r = r
        self.center = center
    def c(self):
        print("周长：", round(2 * math.pi * self.r, 2))
    def s(self):
        print("面积：", round(math.pi * self.r**2, 2))
    def relation_with_point(self, point):
        d = math.sqrt((self.center.x-point.x)**2 + (self.center.y-point.y)**2)
        if d < self.r:
            print("点在圆内")
        elif d == self.r:
            print("点在圆上")
        else:
            print("点在圆外")

center = Point(10, 20)
circle = Circle(10, center)
circle.c()
circle.s()
circle.relation_with_point(Point(20, 20))


# 2.李晓在家里开party，向朋友介绍家中的黄色的宠物狗【彩彩】具有两条腿走路的特异功能。
class Dog:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
    def walk(self):
        return "%s的宠物狗【%s】具有两条腿走路" % (self.fur_color, self.name)

class Person2:
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog
    def introduce(self):
        print("%s在家里开party，向朋友介绍家中的%s的特异功能" % (self.name, self.dog.walk()))

dog = Dog('彩彩', '黄色')
lixiao = Person2('李晓', dog)
lixiao.introduce()

# 3.王梅家的荷兰宠物猪【笨笨】跑丢了，她哭着贴寻猪启示。
class Pig:
    def __init__(self, name, place):
        self.name = name
        self.place = place

class Person3:
    def __init__(self, name, pig):
        self.name = name
        self.pig = pig
    def find(self):
        print("%s家的%s宠物猪【%s】跑丢了，她哭着贴寻猪启示。" % (self.name, self.pig.place, self.pig.name))


# 4.富二代张三向女朋友李四介绍自己的新跑车：白色的宾利
class Rich2Man:
    def __init__(self, name, girl_friend, car):
        self.name = name
        self.girl_friend = girl_friend
        self.car = car
    def introduce(self):
        print("富二代%s向女朋友%s介绍自己的新跑车：%s" % (self.name, self.girl_friend, self.car))

wangsicong = Rich2Man('王思聪', '马蓉', '白色的宾利')
wangsicong.introduce()


# 预习：封装，继承、多态
#
#
#
#
