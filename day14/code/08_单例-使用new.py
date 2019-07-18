

# 设计模式
#    总共23种: 单例模式，桥接模式，代理模式，装饰模式，适配器模式，...
#
# 单例模式：单个实例，用于解决用同一个类创建的多个对象是同一个
#

# 类
class Singleton(object):

    # 构造方法：一般用来初始化属性
    def __init__(self):
        print("__init__")

    # 类属性
    instance = None

    # 创建对象时调用的方法
    @classmethod
    def __new__(cls, *args, **kwargs):
        print("__new__")

        # 第一次调用new方法：cls.instance:False, 所以可以进入if，进入if后会创建对象并赋值给cls.instance
        # 第二次调用new方法: cls.instance:True, 所以不可以进入if，直接返回原来的cls.instance
        # ...
        if not cls.instance:
            print("创建对象")
            # cls.instance = object.__new__(cls, *args, **kwargs)
            cls.instance = super(Singleton, cls).__new__(*args, **kwargs)

        return cls.instance  # 每次返回的都是第一次创建的对象

class Dog(Singleton):
    pass


# 对象
d1 = Dog()
d2 = Dog()

print(id(d1))  # 43680936
print(id(d2))  # 43680936








