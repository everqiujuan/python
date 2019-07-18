

# 模块：其实就是一个.py文件，但是文件名称要遵守命名规范，跟变量的命名类似
#   标准模块, 比如：math, random, os
#   自定义模块，比如：hello
#   第三方模块，比如：pip
#


# 导入模块: 使用import
# 情况1
import os
import os, math

# 用法: 模块名.函数名()
math.sin(10)

# 情况2: 使用自定义模块
import hello

print(hello.age)
hello.login()





