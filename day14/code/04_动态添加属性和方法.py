
# 类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("跑步")

# 对象
p = Person('范冰冰', 39)
print(p.name, p.age)

# 动态添加属性：给当前对象扩展属性
p.sex = "女"
print(p.sex)  # 女
# print(Person('李晨', 40).sex)  # 其他对象没有sex属性


# 动态添加方法
# def sleep1(self):
#     print(self.name, "在睡觉")
# p.sleep = sleep1
# p.sleep(p)

from types import MethodType
def sleep2(self):
    print(self.name, "在睡觉")
p.sleep = MethodType(sleep2, p)
p.sleep()







