''''''

'''
    数据类型
    
    Number: 数值类型
        int: 整型，整数， 1,2
        float: 浮点数，小数, 1.1, 2.2
    String: 字符串类型, "hello"
    Boolean: 布尔类型，True真，False假
    
    None: 空值，特殊类型
    
    List: 列表
    Dict: 字典
    
    tuple: 元组
    set: 集合
    
    bytes: 字节
    
'''

# Number
# int
# a: 变量
# =：赋值
# 10 ： 值
# == : 相等
# type() : 用来输出变量的类型
# id()： 用来输出内存地址
a = 10
print(a)  # 10
print(type(a))  # <class 'int'>， 整数
print(id(a))  # 1786946944, 内存地址

# float
b = 1.2
print(type(b))  # <class 'float'>, 浮点数

# String
c = '宝强'
print(type(c))  # <class 'str'>, 字符串

# Boolean
d = True
print(type(d))  # <class 'bool'>, 布尔类型

# None
e = None
print(type(e))  # <class 'NoneType'>, 空值

# list
f = [1, 2, 3]
print(type(f))  # <class 'list'>, 列表

# dict
g = {"name": "渣渣辉", 'age': 40}
print(type(g))  # <class 'dict'>, 字典

# set
h = {1, 2, 3}
print(type(h))  # <class 'set'>, 集合

# bytes
i = b'hello'
print(type(i))  # <class 'bytes'>, 字节

