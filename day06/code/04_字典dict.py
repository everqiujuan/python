

# 字典dict, dictionary
#
#   列表： 一般保存相同类型的多个数据
#   list = [1,2,3,4]
#
#   字典： 一般保存同一事物的不同类型的数据
#     比如：人是姓名，年龄，qq....
#   dict = {"name": "宝强", "age": 36}
#
#

# 字典dict
person = {"name": "辣子鸡", "age": 20, 'qq': 43242}
print(person)  # {'name': '辣子鸡', 'age': 20, 'qq': 43242}
print(type(person))  # <class 'dict'>

# 列表,不推荐
# person = ["辣子鸡", 20, 43242]

# key: value 键值对
# key:
#   唯一性: 不会存在两个相同名称的key
#   无序的
#   key是不可变类型：string,number,boolean,tuple

person = {'wechat': 'hehe', 'wechat': 'haha', 1: 2, True: False, (1,2): 3}
print(person)  # {'wechat': 'haha'}

# 查
person = {'name': '杰伦', 'age': 39, 'sex': '男', 'height': 1.73}
name = person['name']
print(name)  # '杰伦'
# print(person['qq'])  # 报错  KeyError: 'qq'

# get(): 如果key不存在，则返回None
age = person.get('age1')
print(age)  # None

# 如果key不存在,且有第二个参数，则返回第二个参数
age = person.get('age', 18)
print(age)  # 18


# 增，改
person = {'name': '杰伦', 'age': 39, 'sex': '男', 'height': 1.73}

# 增：如果key不存在
person['qq'] = '123456'
print(person)

# 改：如果key存在
person['sex'] = '女'
print(person)


# 删
person = {'name': '杰伦', 'age': 39, 'sex': '男', 'height': 1.73}

# pop()
person.pop('height')
print(person)

# person.pop('height1')  # 报错，KeyError: 'height1'
res = person.pop('height1', 1.8)
print(person)
print(res)  # 1.8

# popitem(): 随机删除一项，一般都是删最后一值 （了解）
person = {'name': '杰伦', 'age': 39, 'sex': '男', 'height': 1.73}
person.popitem()
person.popitem()
print(person)  # {'name': '杰伦', 'age': 39}

# clear(): 清空字典
person.clear()
print(person)  # {}

person = {'name': '杰伦', 'age': 39, 'sex': '男', 'height': 1.73}
# del person
del person['name']
print(person)  # {'age': 39, 'sex': '男', 'height': 1.73}


# 字典基本操作
# 拼接, 合并
dict1 = {"a": 1}
dict2 = {'b': 2}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2}

# len()
print(len(dict1))  # 2

# in : 判断key
if 'a' in dict1:
    print("a是dict1中的key")


# 遍历
# 方式一： 推荐
for key in dict1:
    print(key)   # key
    print(dict1[key])  # value

# 方式二：不推荐
for i in range(len(dict1)):
    print(i)
# 方式三：不推荐
for i,key in enumerate(dict1):
    print(i, key)

# {'a': 1, 'b': 2}
keys = dict1.keys()  # 获取所有的key
print(keys)  # dict_keys(['a', 'b'])
print(list(keys))  # ['a', 'b']

for key in dict1.keys():  # 遍历所有key
    print(key)

for value in dict1.values():  # 遍历所有value
    print(value)

for k, v in dict1.items(): # 遍历所有key和value
    print(k, v)


# list和dict的区别：
#   list列表:
#       1, 定义方式: [1,2,3], 需要使用下标
#       2, 内存消耗较小
#       3, 数据量增大时，查询速度越慢
#   dict字典：
#       1，定义方式：{key:value}, 需要使用key
#       2, 内存消耗较大
#       3，随着数据量增大，对查询速度影响不大，查询速度快
#
#   表示多个人的信息：
#       [
#           {'name':'', 'age': 90},
#           {'name':'', 'age': 90},
#           {'name':'', 'age': 90},
#           {'name':'', 'likes': [
#                                   'movies': [],
#
#                                 ]
#           },
#       ]
#


