
import re

# 数量
# ? : 表示前面字符出现0次或1次
# + : 表示前面字符出现1次或多次
# * : 表示前面字符出现0次或多次
# {} : 表示前面字符出现的次数范围
# {2,5} : 2-5次
# {2,} : 2次及以上
# {,5} : 最多5次
# {3}: 表示出现刚好3次

#
res = re.findall("g?", "ggoogle")  # ['g', 'g', '', '', 'g', '', '', '']  # 非贪婪模式
res = re.findall("g+", "ggoogle")  # ['gg', 'g']  # 贪婪模式
res = re.findall("g*", "ggoogle")  # ['gg', '', '', 'g', '', '', '']  # 贪婪模式

res = re.findall("g{3}", "ggooggggle")  # ['ggg']
res = re.findall("g{3,}", "ggooggggle")  # ['gggg']
res = re.findall("g{2,3}", "ggooggggle")  # ['gg', 'ggg']
res = re.findall("g{,3}", "ggooggggle")  # ['gg', '', '', 'ggg', 'g', '', '', '']

print(res)




