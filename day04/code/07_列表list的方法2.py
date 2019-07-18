

# index() : 找出指定元素在列表中第一次出现的下标
list1 = [11, 22, 33, 66, 22, 22, 33, 44]
print(list1.index(33))  # 2
# print(list1.index(100))  # 报错, ValueError: 100 is not in list

# 内置函数/内置方法
# max() : 找列表中的最大值
m = max(list1)
print(m)

# min() : 找最小值
print(min(list1))

# sum() : 求和
print(sum(list1))


# 排序
# sort() : 升序，从小到大
list2 = [1, 4, 2, 3, 6, 5, 7, 9, 8]
list2.sort()
print(list2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 降序
list2.sort(reverse=True)
print(list2)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 倒序
# reverse()
list2 = [1, 4, 2, 3, 6, 5, 7, 9, 8]
list2.reverse()
print(list2)


# copy()
# 拷贝，复制
# 赋值
list3 = [1, 2, 3]
list4 = list3
list3[2] = 100
print(list3, list4)  # [1, 2, 100] [1, 2, 100]

# 浅拷贝,浅复制
list3 = [1, 2, 3]
list4 = list3.copy()   # 【掌握】
# list4 = list3 * 1
list3[2] = 100
print(list3, list4)  # [1, 2, 100] [1, 2, 3]

list5 = [1, 2, [3, 4]]
list6 = list5.copy()
list5[2][0] = 99
print(list5, list6)  # [1, 2, [99, 4]] [1, 2, [99, 4]]


# 深拷贝，深复制
import copy
list5 = [1, 2, [3, 4]]
list6 = copy.deepcopy(list5)
list5[2][0] = 99
print(list5, list6)  # [1, 2, [99, 4]] [1, 2, [3, 4]]


# 多维列表
# 一维列表
list1 = [1,2]
# 二维列表
list2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]






