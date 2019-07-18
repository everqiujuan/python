

# 列表生成器: 快速生成列表

# 初始化：定义变量的时候赋值
ages = [1, 2, 3, 4]

ages = []
for i in range(1, 11):
    ages.append(i)
print(ages)

ages = list(range(1, 11))
print(ages)

# 列表生成器
ages = [i for i in range(1, 11)]
print(ages)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ages = [i*i for i in range(1, 11)]
print(ages)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

ages = [i for i in range(1, 11) if i%2]
print(ages)  # [1, 3, 5, 7, 9]

# 100以内50~80之间的所有偶数
ages = [i for i in range(1, 101) if i>=50 and i<=80 if not i%2]
print(ages)


# xyz和abc的所有组合
list1 = ['x', 'y', 'z']
list2 = ['a', 'b', 'c']
ages = [i+j for i in ['x', 'y', 'z'] for j in ['a', 'b', 'c']]
print(ages)  # ['xa', 'xb', 'xc', 'ya', 'yb', 'yc', 'za', 'zb', 'zc']


