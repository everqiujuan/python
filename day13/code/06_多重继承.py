
# 人 Person
# 员工 Employee
# 主管 Manager

# 继承：从一般(父类)到特殊（子类）


# 父类
class Person(object):
    def __init__(s, name):
        s.name = name
        print("Person,self:", id(s))

    def run(self):
        print(self.name, "在跑步")

# 子类
class Employee(Person):
    def __init__(self, name1, age):
        print("Employee,self:", id(self))  # self=employee
        # Person.__init__(self, name1)
        # self.name = name1

        # super() : 表示父类对象
        super().__init__(name1)  # 隐式调用
        self.age = age

    def eat(self):
        print(self.name, "在吃饭")

# 子类对象
Employee("黄峥", 38)
# print("employee:", id(employee))
# print(employee.name, employee.age)
# employee.run()
# employee.eat()

# 山寨货 小米新品的电视机 300块  3亿


# 孙子类
class Manager(Employee):
    def __init__(self, name, age, sex):
        super().__init__(name, age)
        self.sex = sex
    def sleep(self):
        print(self.name, "在睡觉")


#创建孙子类对象
# manager = Manager('黄峥', 38, '男')
# print(manager.name, manager.age, manager.sex)
# manager.run()
# manager.eat()
# manager.sleep()





