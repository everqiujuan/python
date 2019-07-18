

# 构造函数/构造方法

class Person:

    # 类属性，类变量
    # name = "宝强"

    # 魔术方法
    # 构造方法：当创建对象时会自动被调用, 如果不写init方法，默认会自动有一个不包含内容的init方法
    #         作用：初始化属性
    def __init__(self, _name):
        # 对象属性，成员属性，成员变量
        self.name = _name

    # 成员方法
    def run(self):
        print(self.name, "在跑步")

    # 析构函数: 在对象销毁的时候自动被调用
    def __del__(self):
        print("析构函数被调用了，对象马上要被销毁了")

# 对象
p = Person("宋哲")
print(p.name)
# print(Person.name)
p.run()

p2 = Person("宝强")
p2.run()

# del p, p2

print("hello world")
