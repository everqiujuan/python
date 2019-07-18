

# 1.简述必需参数、关键字参数、默认参数、不定长参数的区别
# 必需参数：必需要传的参数，形参数量和实参数量要一致，按顺序
# 关键字参数：在函数调用时，可以通过形参名赋值，可以不按顺序
# 默认参数：形参给默认值，函数调用时可以不用传参
# 不定长参数：
#       *args: 接收多个必需参数（位置参数），会接收一个元组
#       **kwargs: 接收多个关键字参数， 会接收一个字典

# 2.写函数，计算传入字符串中单个【数字】、【字母】、【空格] 以及 【其他】的个数
def fn1(str1):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0

    for ch in str1:
        if ch.isdigit():
            count1 += 1
        elif ch.isalpha():
            count2 += 1
        elif ch == ' ':
            count3 += 1
        else:
            count4 += 1

    return count1, count2, count3, count4

print(fn1("hel1 lo123D F,.,."))


# 3.写函数，判断用户传入的参数（字符串、列表、元组）长度是否大于5
def fn2(t):
    if len(t) > 5:
        return True
    return False

print(fn2("ddd233"))


# 4.写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容("", " ", None)。
# ['    ', '', ' ', None]
def fn3(t):
    for i in t:
        if i in ['', ' ', None]:
            return False
        elif isinstance(i, str) and i.isspace():
            print("是多个空格")
            return False
    return True

print(fn3(['a', '     ', 'b', 33]))


# 5.写一个函数，识别字符串是否符合python语法的变量名
#   数字字母下划线，且不能以数字开头，不能使用关键字
import keyword
def fn4(str1):
    if str1 in keyword.kwlist:
        return False

    if str1[0].isdigit():
        return False

    for ch in str1:
        if not (ch=='_' or ch.isalnum()):
            return False
    return True

print(fn4("hello_123"))


# 6.定义一个函数，传入不定个数的数字，返回所有数字的和
def fn6(*args):
    s = 0
    for i in args:
        s += i
    return s

print(fn6(1,2,3,4))


# 7, 写一个函数计算1到n的和, 并返回结果打印出来;(n为函数参数)
def fn7(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

# 8, 写一个函数计算n的阶乘,并返回结果打印出来
def fn8(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

# 9, 写一个函数计算两个数的最小公倍数; 并返回结果打印出来
def fn9(a, b):
    m = max(a, b)
    for i in range(m, a*b+1):
        if i%a==0 and i%b==0:
            return i

print(fn9(4, 9))  # 12, 24, 48, ...


# 10, 写一个函数判断一个年份是不是闰年
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    return False


# 11, 年月日分别为自定义函数的参数，判断某一个日期是否为合法的日期;
# 	    如: 2018年12月33日不是合法的日期
# 	        2018年11月13日是合法的日期
def fn11(y, m, d):
    # 判断年是否合法
    if y <= 0:
        return False

    # 判断月是否合法
    if m<1 or m>12:
        return False

    # 判断天是否合法
    days = 31
    if m == 2:
        if is_leap(y):
            days = 29
        else:
            days = 28
    elif m in [4, 6, 9, 11]:
        days = 30

    if d>days or d<1:
        return False

    return True

