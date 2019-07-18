
from collections import Iterator  # 迭代器
from collections import Iterable  # 可迭代对象，迭代器对象

# 迭代器
# 迭代器对象：可以使用for-in循环遍历的

# 迭代器对象：可以使用for-in循环的
# list, tuple, dict, set, str, generator对象 都是迭代器对象
print(isinstance([1, 2], Iterable))  # True
print(isinstance((1, 2), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance({1, 2}, Iterable))  # True
print(isinstance("hello", Iterable))  # True
print(isinstance((i for i in range(1,3)), Iterable))  # True


# 迭代器: 可以使用for-in遍历，且可以next()
print(isinstance([1, 2], Iterator))  # False
print(isinstance((1, 2), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance({1, 2}, Iterator))  # False
print(isinstance("hello", Iterator))  # False
print(isinstance((i for i in range(1, 3)), Iterator))  # True


# iter: 可以将迭代器对象 转换成 迭代器
list1 = [11, 22, 33]
res = iter(list1)
# print(res)  # <list_iterator object at 0x00000000027B7208>
# print(next(res))  # 11
# print(next(res))  # 22
# print(next(res))  # 33
# print(next(res))  # 报错

# list(): 将迭代器转换成列表迭代器对象
list2 = list(res)
print(list2)  # [11, 22, 33]



