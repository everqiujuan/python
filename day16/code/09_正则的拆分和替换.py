

# str
#   拆分： split
#   替换： replace

import re

# 正则的拆分
str1 = "hello world bye"
res = re.split(" |l", str1)
print(res)


# 正则的替换
str2 = "特朗普你是大佬，奥巴马也是大佬，习近平是最大佬"
res = re.sub(".{2}大佬", "混混", str2)
print(res)  # "特朗普混混，奥巴马混混，习近平混混"

res = re.subn(".{2}大佬", "混混", str2)
print(res)  # ('特朗普混混，奥巴马混混，习近平混混', 3)


# | : 或
# a|b, x|y
# () : 整体，分组











