

# list的功能或操作
#   增
#   删
#   改
#   查

# 增
# append() : 追加内容 【重点】
list1 = [1, 2]
list1.append(3)
print(list1)  # [1, 2, 3]

# 追加多个元素
# extend()
# list1.append([4, 5])
# print(list1)  # [1, 2, 3, [4, 5]]
list1.extend([4, 5])
print(list1)  # [1, 2, 3, 4, 5]

# insert() : 插入元素
list1.insert(0, 100)
print(list1)  # [100, 1, 2, 3, 4, 5]


# 删除
# pop() : 弹出，默认弹出最后一个【重点】
list2 = ['美国队长', '黑寡妇', '雷神', '钢铁侠', '马斯克', '绿巨人', '蜘蛛侠']
# 马斯克：特斯拉CEO, spaceX CEO, 超级高铁CEO
# res = list2.pop()  # 默认弹出最后一个
res = list2.pop(1)
print(res)
print(list2)

# remove() : 移除
list3 = [11, 22, 33, 44, 22, 22]
res = list3.remove(22)
print(res)  # None
print(list3)  # [11, 33, 44, 22]

# count(): 元素出现的次数
list3 = [11, 22, 33, 44, 22, 22]
print(list3.count(22))  # 3

# 循环删除
for i in range(list3.count(22)):
    list3.remove(22)
print(list3)  # [11, 33, 44]

# del
list4 = [1, 2, 3]
# del list4
del list4[0]
print(list4)

# clear(): 清空
list4 = [1, 2, 3]
list4.clear()
print(list4)  # []


# 改
list5 = [1, 2]
list5[0] = 100  # 【掌握】
print(list5)  # [100, 2]

# 查  【掌握】
print(list5[0])  # 100






