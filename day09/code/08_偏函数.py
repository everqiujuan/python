

# 偏函数(了解)

print(int("10"))  # 10

print(int('1010', base=2))  # 二进制
print(int('1010', base=8))  # 八进制


# 封装一个默认转换为二进制的函数int2
def int2(x):
    return int(x, base=2)

print(int2('1010'))  # 10


# 偏函数
import functools
int3 = functools.partial(int, base=2)
print(int3('1010'))  # 10







