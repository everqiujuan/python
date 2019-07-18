
# 数据类型
#   值类型：
#       Number: 数字， 1, 1.2
#       Boolean: 布尔， True, False
#       String：字符串， "渣渣辉"  序列
#       tuple: 元组，(90, 99, 88, 77,59)
#       None: 空，特殊类型
#   引用类型：
#       list: 列表，[90,99,88,77,59,59]
#       dict: 字典，{'name':'渣渣辉', 'age': 45}
#       set:  集合，{90,99,88,77,59}

# set集合：
#   1，唯一， 元素不会重复
#   2，无序，没有顺序，不能使用索引
#

# 定义set
set1 = {1,2,3,4}
print(set1)  # {1, 2, 3, 4}
print(type(set1))  # <class 'set'>

# 空集合
set1 = set()
print(set1)  # set()
print(type(set1))  # <class 'set'>

# 无序, 不会重复
set2 = {'a', 'b', 'c', 'c', 'c'}
print(set2)  # {'b', 'c', 'a'}

# int()
# float()
# str()
# tuple()
# list()
# dict()
# set()

# set 和 list之间的转换
# 去重
list1 = [1,1,2,2,2,2,3,4,6,5]
set3 = set(list1)
print(list(set3))  # [1, 2, 3, 4, 5, 6]

# set 和 tuple之间转换
tuple1 = (1,2,3)
set4 = set(tuple1)
print(set4)  # {1, 2, 3}
print(tuple(set4))  # (1, 2, 3)

# set 和 string之间的转换
str1 = "hello"
print(list(str1))  # ['h', 'e', 'l', 'l', 'o']
set5 = set(str1)
print(set5)  # {'e', 'h', 'o', 'l'}
print(str(set5))  # "{'o', 'e', 'h', 'l'}"
print(str(True))  # "True"

# set 和 dict之间的转换
dict1 = {'name': '笨小鸡', 'age': 20}
set6 = set(dict1)
print(set6)  # {'age', 'name'}
# print(dict(set6))  # 报错

# dic = dict() # 字面量，直面量
# print(dic)


# set集合
set1 = {11, 22, 33}
print(len(set1))

# 遍历
for n in set1:
    print(n)


# set的操作
# 增
set1 = {11, 22, 33}
set1.add(44)  # 增加一个元素
set1.update([11, 55, 66])  # 添加多个元素
set1.update('abc')
print(set1)  # {33, 66, 'b', 11, 44, 'a', 22, 55, 'c'}

# 删
# pop(): 随机删除一个
set1.pop()
print(set1)

# remove() : 删除指定元素, 不能删除不存在的元素,否则报错
set1 = {11, 22, 33}
set1.remove(33)
print(set1)  # {11, 22}

# discard(): 删除指定元素, 如果不存在，不会报错
set1 = {11, 22, 33}
set1.discard(333)
print(set1)

# clear() : 清空
set1.clear()
print(set1)  # set()


# 集合之间的关系
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 & set2)  # 交集 {3}
print(set1 | set2)  # 并集 {1, 2, 3, 4, 5}
print(set1 - set2)  # 差集 {1, 2}
print(set1 ^ set2)  # 对称差集 {1, 2, 4, 5}
print(set1 > set2)  # 集合1是否包含集合2
print(set1 < set2)  # 集合2是否包含集合1









