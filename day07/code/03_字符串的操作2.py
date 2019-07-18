

# find(): 查找指定子字符串在字符串中第一次出现的下标位置，如果不存在则返回-1
str1 = "helloworld"
print(str1.find('l'))  # 2
print(str1.find("llo"))  # 2
print(str1.find('halo'))  # -1, 没有查找到
print(str1.find('l', 7, 9))  # 在指定范围[7,9)查找第一次出现下标的位置

# rfind(): 从右往左查找第一次出现子字符串的下标位置，如果不存在则返回-1
print(str1.rfind('l'))

# index(): 跟find类似，如果不存在则会报错
print(str1.index('l'))  # 2
# print(str1.index('halo'))  # 报错

# rindex()
print(str1.rindex('l'))  # 8


# 分隔，拆分
# split()：返回一个列表，列表的长度是：分隔字符串数量+1
str1 = "baoqiang is a green man"
print(str1.split())  # ['baoqiang', 'is', 'a', 'green', 'man'], 默认按空格拆分
print(str1.split(" "))  # ['baoqiang', 'is', 'a', 'green', 'man']
print(str1.split("green"))  # ['baoqiang is a ', ' man']
print(str1.split("baoqiang"))  # ['', ' is a green man']
print(str1.split("sex"))  # ['baoqiang is a green man']
print(str1.split('a'))  # ['b', 'oqi', 'ng is ', ' green m', 'n']
# 第2个参数表示只取前面两个a去进行拆分
print(str1.split('a', 2))  # ['b', 'oqi', 'ng is a green man']
# print(list(str1))

# splitlines()：按行拆分
str2 = '''论语
逝者如斯夫
不舍昼夜'''

print(str2.splitlines())  # ['论语', '逝者如斯夫', '不舍昼夜']
print(str2.splitlines(True))  # ['论语\n', '逝者如斯夫\n', '不舍昼夜']


# 合并
# join()
names = ['马云', '马化腾', '马克思', '马斯克', '马赛克']
print("".join(names))  # "马云马化腾马克思马斯克马赛克"
print("+".join(names))  # "马云+马化腾+马克思+马斯克+马赛克"


# replace(): 替换
str3 = "how are are are you"
print(str3.replace("are", "old"))  # "how old old old you"
print(str3.replace("are", "old", 2))  # "how old old are you"


# startswith() : 是否以某子字符串开头
str1 = "hello world"
print(str1.startswith("hello"))  # True

# endswith() : 是否以某子字符串结尾
print(str1.endswith('rld'))  # True


# ASCII码
# chr() : 将ASCII码转为字符
print(chr(65))  # 'A'

# ord() : 将字符转换为ASCII码
print(ord('A'))  # 65


# 编码
# encode(): 编码，将字符串转换成二进制（字节类型）
str1 = "I like 我不是药神"
b = str1.encode()  # 默认是utf-8编码
c = str1.encode('utf-8')
d = str1.encode('GBK')
print(b)
# b'I like \xe6\x88\x91\xe4\xb8\x8d\xe6\x98\xaf\xe8\x8d\xaf\xe7\xa5\x9e'
print(type(b))  # <class 'bytes'>

print(c)
print(d)

# ASCII
# gbk, gb2312
# unicode
# utf-8 : 国际编码，以后都用它

# 解码
# decode()： 将二进制转换成字符串
print(b.decode())
print(c.decode('utf-8'))
print(d.decode('GBK'))


# 简单的加密
t = str.maketrans("aco", "123")
print(t)  # {97: 49, 99: 50, 111: 51}

str1 = "today is a good day"
print(str1.translate(t))  # t3d1y is 1 g33d d1y


# eval():
print(eval("1+1"))
print(eval("-1"))

# a, b = eval(input("请输入两个数字(中间用逗号隔开)："))
# print(a, b)

# eval(): 字符串转换为Python对象
str1 = "[1, 2, 3]"
list1 = eval(str1)
print(list1)  # [1, 2, 3]
print(type(list1))  # <class 'list'>


# json: 显示数据的格式，数据格式
# json字符串： "[1, 2, 3]"
# json对象：[1, 2, 3]





