
#
# 值类型，不可变类型
#   number: 数字
#   string: 字符串
#   boolean: 布尔类型
#   None: 空值类型
#   tuple: 元组
# a = 10
# a = 20

# 引用类型，可变类型
#   list: 列表
#   dict: 字典
#   set: 集合(了解)
# list = [1,2,3]
# list[0] = 100

#
# None: 只有一个值None, 这个类型一般只是用来判断，如果碰到了None则不能继续使用
# 特殊类型
a = None
print(a)

# Boolean: 布尔类型， 两种值：True, False

# Number: 数字类型
#   int 整数
#   float 浮点数
#   complex: 复数（了解）

a = 10
print(type(a))  # <class 'int'>

b = 10.2
print(type(b))  # <class 'float'>

c = "10"
print(type(c))  # <class 'str'>


# int(), float(), str()
# int(): 转成整数
# num1 = 10.2
num1 = "10"
# num1 = "10.2"  # 报错
# num1 = "10abc"  # 报错
print(int(num1))

# float() 转成小数
num2 = "10.3"
# num2 = "10.3abc"  # 报错
print(float(num2))

# str(): 转成字符串
num3 = True
print(str(num3))  # 'True'
print(type(str(num3)))


# 浮点数精度问题
a = 1.1
b = 2.2
c = a + b
print(c)  # 3.3000000000000003










