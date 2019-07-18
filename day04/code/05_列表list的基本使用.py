

#
# 变量：可以存储一个数据
#   表示汽车品牌：car1 = 'benz', car2 = 'BMW', car3 = 'audi'
#   如果有300个品牌呢？
#      使用列表：可以用一个变量存储多个值
#       cars = ['benz', 'BMW', 'audi', ....]

# 【这里都要掌握】

# 创建列表list
list1 = [1, 2, 3, 44]
list2 = ['宝强', '徐峥', '黄渤']
list3 = [1, '周杰伦', True]

print(list1)  # [1, 2, 3, 4]
print(type(list1))  # <class 'list'>

# 列表的下标（索引）,下标从0开始
print(list1[0])  # 1
print(list1[1])  # 2
print(list1[2])  # 3
print(list1[3])  # 4
# print(list1[4])  # 下标越界 ， IndexError: list index out of range
print(list1[-2])  # 倒数第2个

# len() : 获取列表的长度
print(len(list1))  # 4

# 截取，切片
list1 = [11, 22, 33, 44, 55, 66]
print(list1[1:])
print(list1[:3])
print(list1[1:3])  # [22, 33], 下标范围 [1,3)
print(list1[::-1])  # 倒序

# + : 拼接
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)  # [1, 2, 3, 4]

# * ：重复
print(list1 * 2)  # [1, 2, 1, 2]

# in: 判断元素是否在列表中
if 3 in list3:
    print("3是list3中的元素")

