#
# 返回值： return
#   1，如果函数中不写return,默认返回None
#   2, 如果函数中写了return，但不写返回的值, 则会返回None
#   3, 如果函数中写了return，且写了返回的值，则会返回对应的值

def my_sum(a, b):
    s = a + b
    print("return之前的语句")
    return s
    print("return之后的语句")  # 这里不会执行

res = my_sum(10, 20)
print(res)

# l = [1,2]
# n = l.append(3)
# print(n)

# break, continue: 在循环中使用
# return: 在函数中使用

def f1():
    for i in range(3):
        if i == 1:
            return  # 遇到return则立刻结束函数，并返回对应值
        print('i =', i)
    print("for循环结束")

f1()


# 返回多个值
def f2(a, b):
    s1 = a + b
    s2 = a - b
    return s1, s2

print(f2(5, 3))  # (8, 2)


# 判断参数类型
def f3(n):
    # print(type(n))  # <class 'int'>
    if isinstance(n, int):
        print(n, "是整数")
    if isinstance(n, (int, float, bool, list, dict, str, set)):
        print(n, '是int,float,bool,list,dict,str,set中的其中一种类型')


f3(1.1)




# Python中: 一切皆对象


