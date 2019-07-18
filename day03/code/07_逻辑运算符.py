

# 逻辑运算符
# 与：and  或:or  非:not

# and
# 逻辑与：操作数都为True则结果为True, 有假则为假
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or
# 逻辑或： 操作数都为False则结果才为False, 有真则为真
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(3>4 or 4>3)  # True

# not
# 非
print(not False)  # True
print(not True)  # False
print(not 3>4)  # True
print(not 3)  # False

# 为False的值： 0，False, "", [] , None
print(not 0)  # True
print(not "")
print(not None)


# 短路操作
# and: 从左往右依次判断操作数，如果为假，则直接返回为假的值
a = 10 and 11 and 12
print(a)

# or：从左往右依次判断操作数，如果为真，则直接返回为真的值
a = 10 or print(11) or 12
print(a)


# 判断某年份是否为闰年
#    1,能够被4整除且不能被100整除
#  或2，能被400整除
year = 2020
b = (year%4==0 and year%100!=0) or year%400==0
print(b)






