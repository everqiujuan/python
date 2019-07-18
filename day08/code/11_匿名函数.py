

# 匿名函数： 不知道名字的函数
def fn(n):
    return n

f = lambda n:n  # 跟上面的函数定义功能一样
print(f(10))


# 求a+b
f2 = lambda a,b: a+b
# def f2(a, b):
#   return a+b

print(f2(10, 20))

# 用途
persons = [
    {'name': "张三", "age": 33, "score": 90},
    {'name': "李四", "age": 20, "score": 70},
    {'name': "王五", "age": 50, "score": 80},
    {'name': "赵六", "age": 80, "score": 10},
    {'name': "钱七", "age": 70, "score": 30},
]
def fn2(x):
    return x['score']

persons.sort(key=lambda x: x['score'], reverse=True)
print(persons)

# 高阶函数

# 排序方法
def my_sort(l, key=None):
    # 冒泡排序
    for i in range(len(l)-1):
        for j in range(len(l)-1 -i):
            if key(l[j]) > key(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]

# list1 = [11,2,3,4]
# my_sort(list1)
# print(list1)

# def fn2(x):
#     return x['score']
fn3 = lambda dic: dic['age']

my_sort(persons, key=fn3)
print(persons)


# 函数的函数名称： 既是函数的名称，也是指向该函数的变量
def f():
    print(1)

# f()
# 将变量f指向的函数赋值给变量f2，则f2和f都指向该函数
f2 = f
f2()


#
list1 = ["a", "B", 'C', 'F', 'd']
list1.sort(key=str.upper)
print(list1)


