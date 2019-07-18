
# 装饰器

'''
def add():
    print("在hello之前添加的功能")

def hello():
    add()

    print("hello")
    print("world")

    add()

hello()
'''


# 装饰器
def outer(fn):  # fn=say
    def inner():
        print("say之前的代码")
        fn()  # say()
        print('say之后的代码')
    return inner

def say():
    print("我喜欢唱歌")


say = outer(say)  # say2 = inner
say()  # inner()


# def say2():
#     print("say之前的代码")
#     say()


# 装饰器
def sing(fn):  # fn=dance
    def inner():
        print("我喜欢唱歌！")
        fn()   # dance()
    return inner

@sing  # 相当于 dance = sing(dance)
def dance():
    print("我喜欢跳舞")


dance2 = sing(dance)
dance2()  # dance = inner


# 5, 写一个装饰器来统计函数运行的时间
import time

# 用装饰器
def outer(f):
    def fn2():
        start = time.time()
        f()  # fn()
        end = time.time()
        print(end - start)

    return fn2

# 原函数
@outer  # 相当于写上：fn = outer(fn)
def fn():
    for i in range(10000000):
        pass

# fn = outer(fn)  # f=fn
fn()  # fn2()

# @outer  # m = outer(m)
def m():
    print("周杰伦")
    time.sleep(1)
# m = outer(m)
m()

# fn2
'''
def fn2():
    start = time.time()
    fn()
    end = time.time()
    print(end - start)
fn = fn2
'''


# 装饰器
def outer(fn):
    def inner(game):
        print(1)
        res = fn(game)  # 相当于调用原来的play(game)
        print(2)

        return res

    return inner

# @outer
def play(game):
    str1 = "我喜欢玩: %s" % game
    print(str1)
    return str1

play = outer(play)
# play = inner
res = play("吃鸡")  # 相当于: res = inner("吃鸡")
print(res)

