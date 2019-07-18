
import itertools

# 【了解】

# 排列：有顺序
# 排列的可能性：n! / (n-m)!
res = itertools.permutations([1, 2, 3, 4], 2)
print(res)
list1 = list(res)
print(list1)
print(len(list1))

# 组合: 没有顺序
res = itertools.combinations([1, 2, 3, 4], 2)
print(res)
list2 = list(res)
print(list2)
print(len(list2))

#
res = itertools.product("123456789abc", repeat=3)
print(res)
list3 = list(res)
print(list3)
print(len(list3))
