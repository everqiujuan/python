
# 常量： 不可以改变的量
# 变量 ： 可以改变的量， variable

# 定义一个变量
# 声明变量age，且给age赋值10
age = 10
age = 20  # 可以写相同名称的变量，将上面age的值改变成20
print(age)

# 声明/定义多个变量
# a = 10
# b = 20
# a = 10; b = 20  # 不建议这样写
# a, b = 10, 20
a = b = 30   # 先运算=号右边
print(a, b)

# 交换两个变量的值
a = 20
b = 30

#
# c = a
# a = b
# b = c

a, b = b, a
print(a, b)


# 自加1
age = 40
# age = age + 1
age += 1  # 相当于 age = age + 1
# age -= 1  # 相当于 age = age - 1
print(age)

# python 中没有a++, ++a


# 删除变量
sex = '人妖'
del sex
# print(sex)  # NameError: name 'sex' is not defined

# 变量必须先定义再使用
# print(age2)
# age2 = 30


# python是动态类型的语言,弱类型语言
# 弱类型
age = 100
print(type(age))  # <class 'int'>
age = "男"
print(type(age))  # <class 'str'>

# 强类型
# int age = 10， age强制只能赋值整数
# age = "男"








