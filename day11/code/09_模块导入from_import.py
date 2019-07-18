

# from-import

# 模糊导入: 不推荐
# * : 通配符，表示全部
# from hello import *
# print(age)
# login()


# 精确导入
# from hello import age, login
# print(age)
# login()

# from random import randrange
# print(randrange(1,3))
# print(random.randrange(1,3))  # 报错


# 别名
# import random as rd
# print(rd.random())
# print(random.random())  # 报错

from random import randrange as rr
print(rr(1, 3))
# print(randrange(1, 3))  # 报错












