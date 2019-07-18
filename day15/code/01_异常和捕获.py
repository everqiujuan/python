

# 错误： error
#   NameError: 变量未定义
#   TypeError: 类型错误
#   IndexError: 下标越界，索引异常
#   ...
# 异常: exception
#   try-except:
#       当出现异常时，可以捕获异常，让程序后面的代码不受影响
#   try: 尝试执行某段代码
#   except: 如果try中的代码出现异常，则捕获异常

# b = 0
# a = 1 / b  # ZeroDivisionError: division by zero

try:
    a = 1/0
except:
    print("出现异常")

print("end")


try:
    # a = 1/0
    b += 1
    # c = []
    # print(c[2])
except ZeroDivisionError as e:
    print("出现异常：", e)
except NameError as e:
    print("出现异常2：", e)  # name 'b' is not defined


# BaseException: 捕获所有异常
try:
    b += 1/2
except BaseException as e:
    print("出现异常3:", e)


# try-except-else
try:
    b = 1/2
except BaseException as e:
    print("出现异常4")
else:
    print("未出现异常4")

# try-except-finally
try:
    b = 1/0
except BaseException as e:
    print("出现异常5")
finally:
    print("不管是否异常，都会执行我")


# 主动抛出异常
# raise
# raise NameError("哈哈，变量名出错了")
try:
    raise TypeError("类型错了")

except Exception as e:
    print(e)
    # raise


# 异常嵌套
print("我想去拉萨")

try:
    print("我准备坐飞机去拉萨")
    raise Exception("起雾了，飞机航班取消了")

except Exception as e:
    print(e)

    try:
        print("我准备骑自行车去")
        raise Exception("下冰雹了，骑自行车去不了")
    except Exception as e:
        print(e)
        print("我走路去拉萨")
        print("到拉萨了，拉萨很漂亮")


# 自定义异常
class MyException(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return self.msg

    def handle(self):
        print("出现异常")

try:
    raise MyException("自定义的异常")

except MyException as e:
    print(e)
    e.handle()


# 断言 assert: 预测
def fn(n):
    # 预测n!=0， 如果n==0跟预测的不一样，则会报错
    assert n != 0, "n等于0"  # AssertionError: n等于0
    b = 1/n

fn(0)





