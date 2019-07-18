

# 文件操作：
#   1，打开文件
#   2, 操作文件：读（read）、写（write）
#   3, 关闭文件


# 1, 打开文件
# 默认打开文件时的编码是：gbk
# fp = open('hello.txt', encoding='utf-8')

# 2, 操作文件
# 读 read
# print(fp.read())

# 3, 关闭文件
# fp.close()


# 打开方式：
#   mode: 打开方式， 默认是'r'
#       r: 只读，文件不存在会报错 【掌握】
#       rb: 只读二进制，文件不存在会报错【掌握】
#       r+: 在r的基础上，可以写
#       rb+: 在rb的基础上，可以写
#
#       w: 清空写
#       w: 只写，文件不存在会自动创建【掌握】
#       wb: 只写二进制，文件不存在会自动创建【掌握】
#       w+: 在w的基础，可以读
#       wb+: 在wb的基础上，可以读
#
#       a: 不清空，只追加
#       a: 只写(追加)，文件不存在会自动创建【掌握】
#       ab: 只写二进制(追加)，文件不存在会自动创建【掌握】
#       a+: 在a的基础，可以读
#       ab+: 在ab的基础上，可以读


# fp = open('hello.txt', mode='r', encoding='utf-8')
# fp = open('hello.txt', mode='rb')
# fp = open('hello.txt', 'w', encoding='utf-8')  # 打开时就会清空内容
# fp = open('hello.txt', 'wb')
# fp = open('hello.txt', 'a', encoding='utf-8')
fp = open('hello.txt', 'ab')

# r
# content = fp.read()  # 读取所有内容
# content = fp.read(3)  # 读取前面3个字符
# content = fp.readline()  # 读取下一行
# content = fp.readline()  # 读取下一行
# content = fp.readlines()  # 按行读取，返回一个列表
# content = fp.read()
# print(content.decode())

# w
# fp.write("hello")
# fp.write("hello".encode())

# a
# fp.write("hello")
fp.write("hello".encode())


fp.close()

