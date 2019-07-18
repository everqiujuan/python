

# 函数
#   封装功能，利于维护，重复使用，包含作用域，不调用不执行。

# fn：既是函数名称， 也是指向该函数的变量

def fn():
    print("fn")

print(fn)  # <function fn at 0x0000000000523E18>

fn2 = fn
fn2()   # 只要是指向该函数的变量，都可以加括号来调用


# 作用域： 起作用的范围
#   全局变量：所有函数都可以使用的变量
#   局部变量：局部作用域内可以使用的变量

# 局部变量
def fn3():
    b = 10  # b变量的作用域只在函数fn3内部，局部变量
    print(b)

fn3()
# print(b)  报错


# 全局变量
c = 20
def fn4():
    print(c)  # 20

fn4()
print(c)  # 20

# if , for , while都不包含作用域
# if True:
#     a = 10
# print(a)


# global
d = 100
def fn5():
    # 会打印200，d=200是局部变量，不是修改函数外的d
    # d = 200
    # print("d =", d)  # 200

    # d += 1  # 会报错

    global d  # 表示使用全局变量d
    # d = 200
    d += 1
    print("d =", d)

fn5()
print("d2=", d)  # 200

