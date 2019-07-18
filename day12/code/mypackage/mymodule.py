# 1. 使用冒泡排序对列表进行降序排序
# 			def fn(l):

def fn1(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1-i):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

# 2. 使用选择排序对列表进行升序排序
def fn2(l):
    for i in range(len(l)-1):
        minIndex = i
        for j in range(i+1, len(l)):
            if l[j] < l[minIndex]:
                minIndex = j
        l[i], l[minIndex] = l[minIndex], l[i]


# 3. 查找列表的元素
# 	找到返回下标, 找不到返回-1
# 	def fn(l, n):
def fn3(l, n):
    for i in range(len(l)):
        if l[i] == n:
            return i
    return -1


# 4.使用顺序查询，获取列表中所有与指定元素重复的元素脚标
#   def fn(l, n):
def fn4(l, n):
    list1 = []
    for i in range(len(l)):
        if l[i] == n:
            list1.append(i)
    return list1





