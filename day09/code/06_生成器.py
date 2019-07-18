
# 列表生成器
#   [i for i in range(1, 11)]
# list1 = [1,2,3,..]

# 生成器
genarator = (i for i in range(1, 4))
print(genarator)  # 生成器对象 <generator object <genexpr> at 0x000000000297AD00>

# next() : 下一个，获取下一个元素
# print(next(genarator))  # 1
# print(next(genarator))  # 2
# print(next(genarator))  # 3
# print(next(genarator))  # 报错， StopIteration

# 遍历
for i in genarator:
    print('i =', i)


# 生成器函数: 普通函数中包含yield就是生成器函数
def fn(n):
    print("hello")
    yield n+1

    print("你好")
    yield n+2

genarator = fn(10)
# print(genarator)  # <generator object <genexpr> at 0x000000000297AD00>

# 使用next()调用
# print(next(genarator))  # 11
# print(next(genarator))  # 12
# print(next(genarator))  # 报错， StopIteration





