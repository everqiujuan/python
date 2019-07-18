
# name = input("请输入你的名字:")
# print(int(name) + 2)
# print(type(name))  # <class 'str'>

# int() : 转换成整数
print(int(10))
print(int(10.1))
print(int("10"))
# print(int("10.1"))  # 报错
# print(int("abc"))  # 报错

# float(): 转换成小数
print(float(10))
print(float(10.1))
print(float("10"))
print(float("10.1"))
# print(float("abc"))  # 报错

# str(): 转换成字符串

age = int(input('请输入您的年龄:'))
height = float(input("请输入您的身高:"))

# 占位符：%d整数, %s字符串, %f小数
print('姓名:%s, 年龄:%d, 身高:%f' % ("古天乐", age, height))
print('身高：%f' % height)
print('身高：%.2f' % height)  # 小数点后保留2位小数
