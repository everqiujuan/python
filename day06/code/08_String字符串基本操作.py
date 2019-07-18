

#
#  字符串： 一串字符，用单引号或双引号包裹的内容就是字符串
#

# 字符串的定义
name = '昆凌'
movie = '摩天营救'
age = 25
sex = '性别是"女"'

# 单双引号交替使用

# + : 拼接字符串
str1 = name + movie + str(age) + sex
print(str1)

# * :  复制，重复
print(name * 3)

# 下标
str2 = "hello"
print(str2[0])  # h
print(str2[1])  # e
print(str2[2])  # l
print(str2[3])  # l
print(str2[4])  # o
# print(str2[5])  # 报错 下标越界 IndexError: string index out of range
print(str2[-1])  # 倒数第一个

# 字符串不可以修改，如果需要修改，则重新复制新字符
# str2[0] = 'a'  # 不可变类型
str2 = 'halo'

# len(): 字符串长度
print(len(str2))

# 切片
str3 = "helloworld"
print(str3[3:6])
print(str3[::-1])  # 倒序

# in: 判断子字符串是否出现在字符串中
print('llo' in str3)  # True

# 占位符 %d, %s, %f(%.2f)
print("姓名：%s, 年龄: %d, 身高:%.2f" % (name, age, 1.639))

# 遍历字符串
for ch in str3:
    print(ch)
for i in range(len(str3)):
    print(i, str3[i])


# 字符串转义
# \n : 换行
# \t : 制表符，tab
print("hello\nworld")

print("""hello
world""")

# \ : 让有语义的字符变得没有语义
print("\"")

print("C:\Windows\System32\trivers\etc")  # C:\Windows\System32	rivers\etc
print("C:\\Windows\\System32\\trivers\\etc")  # C:\Windows\System32\trivers\etc

# r"" : 会将字符中有语义的字符变成没有语义
print(r"C:\Windows\System32\trivers\etc")  # C:\Windows\System32\trivers\etc

# replace() : 替换
str1 = "hello world 你好"
str2 = str1.replace("hello", "+")
print(str1)  # hello world 你好
print(str2)  # hello+world+你好


