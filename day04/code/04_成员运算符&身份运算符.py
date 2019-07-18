

# 成员运算符
#   in, not in
names = ['林志玲', '范冰冰', '渣渣辉', '马龙', '凤姐']
girlfriend = '范冰冰'
if girlfriend in names:
    print("我女朋友是", girlfriend)
if girlfriend not in names:
    print('我女朋友不是', girlfriend)


# 身份运算符
#    is, is not
#  判断内存地址
a = 10
b = a

print(id(a))  # 1786946944
print(id(b))  # 1786946944
print(a is b)  # True
print(a is not b)  # False
print(a == b)


# 值类型：不可变类型， number,string,boolean
# 只是简单的赋值，两个变量没有关联
a = 10
b = a
b = 20
print(a, b)  # 10, 20

# 引用类型, list, dict
# 赋值后有关联
list1 = [1, 2]
list2 = list1
list2[1] = 99
print(list1, list2)  # [1, 99] [1, 99]



