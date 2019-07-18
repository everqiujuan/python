
# 字符串长度和数量
str1 = "hello hello"
print(len(str1))  # 11
print(str1.count('ll'))  # 2
# print(str1.count('ll', 0, 5))  # 1

# 大小写转换
str1 = "HELLO world"
print(str1.upper())  # HELLO WORLD
print(str1.lower())  # hello world

# title(): 标题化，每个单词的首字母大写
print(str1.title())  # Hello World

# capitalize(): 整个字符串的首字母大写,其他小写
print(str1.capitalize())  # Hello world

# swapcase() : 大小写翻转
print(str1.swapcase())  # hello WORLD


# 对齐方式
# zfill(): 让字符串总长度为40，str1靠右，其他用0填充
print(str1.zfill(40))

# center()： 居中显示字符串，其他地方默认用空格填充
print(str1.center(40))
print("华丽的分割线".center(60, '*'))

# ljust() : 靠左
print(str1.ljust(60, "-"))

# rjust() : 靠右
print(str1.rjust(60, '-'))


# 判断
# isupper(): 判断是否为大写
print("HELLO".isupper())
print('H'.isupper())

# islower(): 判断是否为小写
print('helo'.islower())

# isalpha(): 判断是否都是字母
print("hello".isalpha())

# isalnum(): 判断是否都是字母或数字
print("hello3".isalnum())

# isdigit(): 是否为数值型字符串
print('33'.isdigit())
print('4'.isdigit())

# istitle(): 是否为标题化的字符
print("Hello Wrold".istitle())


# 提取
# strip()：去掉首尾的指定内容，提取出中间的内容
str1 = "    韩   信      "
print(str1.strip())  # "韩   信" ， 默认去掉首尾空格

str2 = "------不--知--火--舞-------"
print(str2.strip('-'))  # 不--知--火--舞

# lstrip(): 去掉左边(首)的指定内容
print(str2.lstrip('-'))  # 不--知--火--舞-------

# rstrip(): 去掉右边(尾)的指定内容
print(str2.rstrip('-'))  # ------不--知--火--舞


