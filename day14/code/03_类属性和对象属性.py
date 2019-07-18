#
class Person:

    # 类属性: 可以用类或对象来调用，建议用类名调用
    #  类属性是共享的：同一个类创建的不同对象使用同一个类属性
    name = "宝强"
    family = ["爸爸",'妈妈','哥哥']
    age = 100

    def __init__(self, age):
        # 对象属性/成员属性/成员变量：需要用对象来调用
        self.age = age
        self.family2 = ["爸爸", '妈妈', '哥哥']

# 对象
p = Person(33)
# print(p.name)
# print(Person.name)
# print(p.age)
# print(Person.age)  # 报错

print(p.age)  # 33  优先使用对象属性
print(Person.age)  # 100
p.name = "老宋"  # 动态添加属性
print(p.name)  # 老宋
print(Person.name)  # 宝强

# p1 = Person(44)
# print(Person.name)  # '宝强'
# print(p1.age)  # 44

# p2 = Person(55)
# print(Person.name)  # '宝强'
# print(p2.age)  # 55

# p3
p3 = Person(30)
p4 = Person(40)
print(p3.family)  # ['爸爸', '妈妈', '哥哥']
print(p4.family)  # ['爸爸', '妈妈', '哥哥']
p3.family.append("妹妹")
print(p3.family)  # ['爸爸', '妈妈', '哥哥', '妹妹']
print(p4.family)  # ['爸爸', '妈妈', '哥哥', '妹妹']

p5 = Person(50)
print(p5.family)

# 对象属性
p6 = Person(60)
print(p6.family2)  # ['爸爸', '妈妈', '哥哥']
p6.family2.append("妹妹")
print(p6.family2)  # ['爸爸', '妈妈', '哥哥', '妹妹']
p7 = Person(70)
print(p7.family2)  # ['爸爸', '妈妈', '哥哥']


