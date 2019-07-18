
import re

# 匹配单个字符

# . : 表示匹配任意单个字符，除了换行
pattern = "go.gle"
str1 = "go5gle"
res = re.search(pattern, str1)
res = re.search("go.gle", "go\ngle")  # None
res = re.search("go.gle", "go\ngle", re.S)  # 可以匹配到
print(res)

# [] : 表示单个字符的范围
# [abc] : 表示单个字符可以为a或b或c
# [a-z] : 表示a到z中的任意一个，小写字母
# [A-Z] : 表示大写
# [a-zA-Z] : 表示字母
# [0-9] : 数字
# [a-zA-Z0-9_] : 数字字母下划线
res = re.search("go[abc123]gle", 'go3gle')
res = re.search("go[a-z]gle", 'gobgle')
res = re.search("go[a-zA-Z0-9_,]gle", 'go,gle')
print(res)


# \d : 表示数字，等价于：[0-9]
# \D : 表示非数字，等价于： [^0-9]
# \w: 表示数字字母下户线，等价于：[a-zA-Z0-9_]
# \W: 表示非数字字母下户线, 等价于：[^a-zA-Z0-9_]
# \s: 表示空格，换行\n, 制表符\t, 换页符：\f, 回车符:\r, 等价于：[ \n\t\f\r]
# \S: 非空格\n\t\f\r , 等价于：[^ \n\t\f\r]

# \d
res = re.search('go\dgle', 'go4gle')
res = re.search('go\Dgle', 'go,gle')
res = re.search('go[^0-9]gle', 'go,gle')
# \w
res = re.search('go\wgle', 'go_gle')
res = re.search('go\Wgle', 'go,gle')
# \s
res = re.search('go\s\sgle', 'go \ngle')
res = re.search('go\Sgle', 'go gle')

print(res)

# 单个字符重点掌握
# . [] \d \w \s


# 边界字符
# ^ : 是否以指定正则表达式开头，开头匹配
# $ : 是否以指定正则表达式结尾，结尾匹配
# ^pattern$ : 完全匹配
# \A : 是否以指定正则表达式开头，开头匹配
# \Z : 是否以指定正则表达式结尾，结尾匹配
# \Apattern\Z : 完全匹配

#
res = re.search('^google', 'google123')
res = re.search('google$', '123google')
res = re.search('^google$', 'google')
res = re.search('^go.*gle$', 'goabcd123gle')
print(res)

res = re.search('\Agoogle', 'google123')
res = re.search('google\Z', '123google')
res = re.search('\Agoogle\Z', 'google')
print(res)

# 区别
# ^$ : 在换行模式re.M下，每一行会重新用正则匹配
res = re.findall('\A#', '#baidu\n#google\n#360搜索', re.M)  # ['#']
res = re.findall('^#', '#baidu\n#google\n#360搜索', re.M)  # ['#', '#', '#']
print(res)


# \b : 匹配单词边界, 是否是以某字符串结尾
# \B : 匹配单词是否不是以某字符串结尾
res = re.search(r"google\b", "google123 abcgoogle abcgoogle123")
res = re.search(r"google\B", "abcdgoogle abcgoogle abcgoogle123")
print(res)


# 单个字符重点掌握
# . [] \d \w \s
# ^, $, ^$








