

# {}: 表示次数范围
# []: 表示单个字符范围
# (): 整体，分组

import re

#
str1 = "0755-88888888"
pattern = "(\d{4})-(\d{8})"
# pattern = "(\d{4})-(?:\d{8})"  # (?:\d{8}) : 非捕获性分组，不能被捕获到
res = re.search(pattern, str1)
# print(res)

# group(): 获取分组的内容
print(res.group())  # 0755-88888888
print(res.group(0))  # 0755-88888888
print(res.group(1))  # 0755，获取第1个分组(第1个括号)的内容
print(res.group(2))  # 88888888，获取第2个分组(第2个括号)的内容
# print(res.group(3))  # 报错

# groups(): 获取所有分组的内容，返回一个元组
print(res.groups())  # ('0755', '88888888')

# 分组的别名
str1 = "0755-88888888"
pattern = "(?P<first>\d{4})-(?P<second>\d{8})"
res = re.search(pattern, str1)
print(res.group('first'))  # 0755
print(res.group('second'))  # 88888888
print(res.group(1))  # 0755
print(res.group(2))  # 88888888


# findall(): 直接获取捕获的分组内容
str1 = "0755-88888888"
pattern = "(\d{4})-(\d{8})"  # [('0755', '88888888')]
pattern = "(\d{4})-\d{8}"  # ['0755']
pattern = "\d{4}-\d{8}"  # ['0755-88888888']
res = re.findall(pattern, str1)
print(res)


# 正则的编译:
#   效率高一点
# 编译正则
com = re.compile("g.*gle")
res = com.search("google")
print(res)

# com.match()
# com.search()
# com.findall()

# \.: 转义字符, 将有语义的字符变成没有语义
print(re.search('\w+@\w+.\w+', "jack@163lcom"))
print(re.search('\w+@\w+\.\w+', "jack@163.com"))

print(re.search("\[\\n\]", "[\n]"))


# findall():
res = re.findall("\d+","12 fjhaehgj 66 fhaj  ")
print(res)  # ['12', '66']
print()

#finditer(): 返回的结果为可迭代器
iter = re.finditer(r"\d+","12 fjhaehgj 66 fhaj  ")
print(iter)
for i in iter:
    print(i)
    #获取值
    print(i.group())
    #获取下标
    print(i.span())




# 正则的方法
# re.match() : 开头匹配
# re.search() : 查找字符串是否存在指定正则的内容
# re.findall() : 查找到并返回所有内容，返回列表

# 正则的符号
# 单个字符
# . 表示除了换行以外的任意单个字符
# []: 表示字符出现的范围
#   [abc]
#   [a-z]
#   [^a-z]
# \d : 数字
# \D : 非数字
# \w : 数字字母下划线
#   \w+ :表示字符串
# \W : 非数字字母下划线
# \s: 空格\n,\t,\f,\r
# \S: 非空格\n,\t,\f,\r

# 边界
# ^: 开头匹配
# $: 结尾匹配
# ^ $: 完全匹配
# \A
# \Z
# \A \Z
# \b : 单词边界
# \B

# 次数
# ?: 表示0或1次
# +：1次或多次
# *：0次或多次
# {}：次数范围
#   {5}：5次
#   {5,7}：5-7次
#   {5,}: 最少5次
#   {,7}: 最多7次

# (): 分组
#   两个作用： 1为了整体，2为了捕获内容

# 编译：
# res = re.compile(pattern)
# res.search()
# res.findall()
# res.match()



