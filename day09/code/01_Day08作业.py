#
# 【以下功能都使用函数封装】
#
# 初级
# 1.计算从1到某个数以内所有奇数的和并返回
def fn1(n):
    s = 0
    for i in range(1, n+1):
        if i%2:
            s += i
    return s

res = fn1(100)
print(res)


# 2.判断某个数是否是偶数，返回结果
def fn2(n):
    if n%2 == 0:
        return True
    return False

print(fn2(10))


# 3.判断某个数是否是素数，返回结果
def fn3(n):

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

print(fn3(77))


# 4.计算2-100之间素数的个数，返回结果
def fn4():
    count = 0
    for i in range(2, 101):
        if fn3(i):
            count += 1
    return count

print(fn4())


# 中级
# 1.比较某两个数的大小，返回较大的一个
def fn5(a, b):
    return max(a, b)

print(fn5(20, 30))


# 2.交换某两个变量的值
def fn6(a, b):
    # a, b = b, a
    return b, a

m = 10
n = 20
m, n = fn6(m, n)
print(m, n)


# 3,封装函数，将某个字符串中的大写字母转换为小写，小写字母转换为大写，将新的字符串返回【参数设置为默认参数】
def fn7(str1="aB"):
    return str1.swapcase()

print(fn7("DFdfsd"))


# 高级
# 1,定义函数实现如下要求
# 	例如：输入2，5，则求2+22+222+2222+22222的和
def fn8(a, n):
    s = 0
    temp = 0
    for i in range(n):
        temp = temp*10 + a
        s += temp
    return s

print(fn8(2, 5))


# 2,已知千锋邮箱的用户名只能由数字字母下划线组成，域名为@1000phone.com,
#    写一个函数isLegalEmail，判断一个字符串是否是千锋邮箱，是返回True，不是返回False。
#      ma@il@1000phone.com  是
#      mail$@1000phone.com  不是
#      mail@1000phone.comp  不是

def isLegalEmail(email):

    list1 = email.split('@')
    if len(list1) != 2:
        return False

    if list1[1] != "1000phone.com":
        return False

    for ch in list1[0]:
        if not (ch=='_' or ch.isalnum()):
            return False
    
    return True

print(isLegalEmail('mail@1000phone.com'))