

# 回调函数 （扩展）

# 函数定义
def f1(n, fn):  # fn = callback
    print("n =", n)

    a = n*n
    fn(a)  # callback() 回调


# 函数调用，
# 回调函数
def callback(a):
    print("callback, a =", a)

# 正向调用
f1(2, callback)


# 进程：正在运行的软件
# 线程：进程中的多个分支
# 同步：在同一个线程中执行
# 异步：在不同的线程中执行




