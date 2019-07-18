''''''

# 简答题
# 1， Python中的循环有几种:
# while, for

# 2， Python的数据类型有哪些:
# number, boolean, string, list, tuple, dict, set, bytes, None

# 3， Python中空类型特殊值是: None


# 4， 判断下列赋值方式正确与否（True or False）
'''
    x = y = z = 1           =>  True
    x=1, y=2                =>  False
    x, *y, z = 1,2,3,4      =>  True
    x, y, z = (1,2,3)       =>  True
'''
x, *y, z = 1,2,3,4
print(x, y, z)  # 1 [2, 3] 4

# 5, 列举5种常用的内置函数：
# int(), float(), pow(), max(), min(), sum(), list(), tuple(), next(), len(), range()
# id(), print()

# 6，判断下面变量名不正确的有哪些：
# ABC, aBC, a-bc, a_bc， _num123, 123num, NUM123, num_123，
# True, false, true1, false0， print, id, __id__, python
# 不正确的有哪些: a-bc, 123num, True
# print(1)
# print = 10
# print(11)  # 报错
# python = 10


# 7， 列举列表list中的至少6个函数，且说明每个函数对应的作用
# list.append(): 追加一个元素
# list.extend([1,2]): 追加多个元素
# list.insert(index, n)： 在index位置插入元素n
# list.pop(): 弹出最后一个元素
#   list.pop(index)
# list.remove(n) : 删除指定元素
# list.count(n): n出现的次数
# list.sort(): 排序，升序
#   list.sort(reverse=True): 降序
# list.reverse() : 倒序
# list.copy() : 复制
# list.index()


# 8， 列举字典dict中的至少3个函数，且说明每个函数对应的作用
# dict.get(key): 获取指定key的值
# dict.update(dict2): 拼接
# dict.pop(key): 删除指定key
# dict.popitem() ：随机删除一个元素
# dict.keys()
# dict.values()
# dict.items()


# 编程题
# 1， 将列表中元素去重， 使用至少3种方式


# 2、编写一个函数gcd(x,y) 求最大公约数，编写一个函数lcm(x,y)求最小公倍数。
# 最大公约数
def gcd(x, y):
    m = min(x, y)
    for i in range(m, 0, -1):
        if x%i==0 and y%i==0:
            return i

# 最小公倍数
def lcm(x, y):
    return x * y / gcd(x, y)

print(gcd(6, 9))
print(lcm(6, 9))


# 3、使用Python编程实现下面图形打印：
'''
     *     i=1  4
    **     i=2  3
   ***     i=3  2
  ****     i=4  1
 *****     i=5  0
'''
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end='')
    for k in range(i):
        print("*", end='')
    print()

# 4、使用Python编程实现下面图形打印：
'''
     *        i=1    1
    ***       i=2    3
   *****      i=3    5
  *******     i=4    7
 *********    i=5    9
'''
for i in range(1, 6):
    for j in range(5-i):
        print(" ", end='')
    for k in range(2*i-1):
        print("*", end='')
    print()


# 5， 将字典的key和value置换，
# 如使用字典 d1 = {'a':1,'b':2,'c':3}，
#   生成字典 d2 = {1:'a', 2:'b', 3:'c'}
d1 = {'a':1,'b':2,'c':3}
d2 = {}
for k, v in d1.items():
    d2[v] = k
print(d2)


# 6、使用Python写一个按照下面方式调用都能正常工作的 my_sum() 方法
'''
    print(my_sum(2,3))     输出 5
    print(my_sum(2)(3))    输出 5
'''
def my_sum(*args):
    if len(args) > 1:
        return sum(args)
    else:
        n = args[0]
        def f(m):
            return n + m
        return f

print(my_sum(2, 3))

# print(my_sum(2)(3))
f2 = my_sum(2)  # f2=f
print(f2(3))  # f2(3) : f(3)


# 7， 封装函数，传入不定数量的数值型参数，返回所有数字的乘积
def fn(*args):
    s = 1
    for i in args:
        s *= i
    return s


# 8， 封装一个函数random_color，该函数的返回值为随机十六进制颜色。
# 说明： 十六进制颜色#开头后面接6个十六进制数， 例: #FFFFFF， #000000， #0033CC
# colors = ['0','1','2',..'F']
import random
def random_color():
    colors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    str1 = '#'
    for i in range(6):
        str1 += random.choice(colors)
    return str1

print(random_color())

# red green blue
# #089F4A
#  08 红色
#  9F 绿色
#  4A 蓝色

# 00-FF: 0~255
# 16*15+15 + 17*15=255


# 9， 封装函数，
# 第一个函数create_persons(), 创建并返回包含5个字典(例如:{"name":"xx","age":xx, "faceValue":100})的列表
#                           其中name的值：从["张三","李四","王五","赵六","钱七"]依次取
#                           其中age的值：10-100之间的随机整数
#                           其中faceValue的值：0-100之间的随机整数
# 第二个函数get_old(), 传入第一个函数创建的列表, 找出列表中年龄最大的人，并将其所有信息打印
# 第三个函数sort_facevalue(), 传入第一个函数创建的列表, 根据颜值升序排列，并打印排序后的信息

def create_persons():
    names = ["张三","李四","王五","赵六","钱七"]
    list1 = []
    for i in names:
        name = i
        age = random.randrange(10, 101)
        faceValue = random.randrange(0, 101)
        dic = {'name': name, 'age': age, 'faceValue': faceValue}
        list1.append(dic)
    return list1


def get_old(persons):
    max_age_dic = max(persons, key=lambda d: d['age'])
    max_age = max_age_dic.get('age')

    for p in persons:
        if p.get('age') == max_age:
            print(p)
    print()

def sort_facevalue(persons):
    persons.sort(key=lambda d:d['faceValue'])
    print(persons)

# 调用
persons = create_persons()

get_old(persons)
sort_facevalue(persons)






