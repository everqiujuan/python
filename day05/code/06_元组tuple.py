

# 列表list: list = [1,2,3,4]
#       1，有序
#       2，可以重复
#       3, 元素可以修改
# 元组tuple:
#       1，元素不可以改变
#       2, 有序
#       3，可以重复

#   NSArray 不可变数组
#   NSMutableArray 可变数组

# 元组： 不可变
t = (1, 2, 3)
print(t)
print(type(t))  # <class 'tuple'>

# 增，删，改
# 元组不可以改变
# t[0] = 100  # 报错

# 如果一定要改变，则转换成列表
# int(), float(), str(), list(), tuple(), dict(), set()
l = list(t)
print(l)  # [1, 2, 3]

# 查
t = (1, 2, 3)
print(t[0])
print(t[1])
print(t[2])
# print(t[3])  # 下标越界， 报错
print(t[-1])

# a, b, c = 1, 2, 3
a, b, c = t
print(a, b, c)

# 遍历
for n in t:
    print(n)

for i in range(len(t)):
    print(i)

for i,n in enumerate(t):
    print(i, n)

# index() : 查找某元素在元组中第一次出现的下标
t = (1, 2, 3, "hello", 2, 3, 4)
print(t.index(3))  # 2


# 只有一个元素的元组
t1 = (3,)  # (3)
print(t1)
print(len(t1))  # 1


# 可以修改元组内部的引用类型数据
t2 = (1, 2, [3, 4])
# t2[1] = 100  # 报错
t2[2][0] = 300
print(t2)  # (1, 2, [300, 4])


# 元组的基本操作
# + 合并，拼接
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # (1, 2, 3, 4)

# len(): 获取元素个数
print(len(t1))

# * : 重复
print(t1 * 2)  # (1, 2, 1, 2)

# in: 成员
print(2 in t1)  # True

# [:] : 切片，截取
t3 = (1,2,3,4,5,6,7)
print(t3[2:6])  # (3, 4, 5, 6)
print(t3[::-1])  # (7, 6, 5, 4, 3, 2, 1)
print(t3)  # (1, 2, 3, 4, 5, 6, 7)

print(tuple([1,2,3]))  # (1, 2, 3)

print(max(t3), min(t3))

# 排序
t1 = (11, 28, 3)
t2 = sorted(t1)  # 升序
print(t2)  # [3, 11, 28]
print(t1)  # (11, 28, 3)

# 降序
t3 = sorted(t1, reverse=True)
print(t3)  # [28, 11, 3]

# 倒序
t4 = reversed(t1)
print(list(t4))  # [3, 28, 11]


