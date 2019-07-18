

# 数值操作
# max()
print(max(2,3,6,5))

# min()
print(min(2,3,-6,5))

# abs(): 绝对值
print(abs(-3))

# round(): 四舍五入
print(round(34.467))  # 34
print(round(34.456, 2))  # 34.46

# math模块
import math

# 次方
print(math.pow(2, 3))  # 8.0
print(pow(2, 3))  # 8
print(2 ** 3)  # 8

print(math.ceil(3.1))  # 向上取整
print(math.floor(3.9))  # 向下取整

print(math.sqrt(64))  # 开平方根

print(math.sin(math.pi))  # 正弦
print(math.pi)  # π

# math.cos()
# math.tan()
# math.asin()
# math.acos()
# math.atan()
# math.log()


# cos()

# 随机数
import random

# random.choice(): 从指定的序列中选择一个
list1 = ['林志玲', '凤姐', '马蓉', '白百何', '范冰冰']
name = random.choice(list1)
print(name)

age = random.choice(range(10, 30))
print(age)

# range() 详解
'''
# 一个参数
for i in range(3):  # 0-2
    print(i)

# 两个参数
for i in range(2, 4):  # 2-3
    print(i)

# 三个参数
for i in range(1, 7, 2):
    print('i=', i)

for i in range(7, 1, -2):
    print('i2=', i)

# 切片
list1 = [1,2,3,4,5,6,7]
print(list1[::-1])  # 倒序
print(list1[5:2:-1])

'''


# random.randrange(start,end,step): 随机获取指定范围内的整数,范围[start, end)
print(random.randrange(2, 10))  # 2-9
print(random.randrange(2, 10, 2))  # 从2,4,6,8中获取一个

# random.randint(start, end): 随机获取[start, end]中的一个整数
print(random.randint(5, 6))  # [5, 6]

# random.random(): 随机获取一个[0,1)的小数
print(random.random())

# random.uniform(start, end): 随机获取[start, end]中的一个小数
print(random.uniform(2, 10))

# random.shuffle() : 乱序
list1 = [1,2,3,4,5]
random.shuffle(list1)
print(list1)
