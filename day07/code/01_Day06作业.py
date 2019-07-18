import random

# 初级：
# 1.已知字符串：“this is a test of Python”
# 	a.统计该字符串中字母s出现的次数
# 	b.取出子字符串“test”   str.find('test')
# 	c.采用不同的方式将字符串倒序输出
# 	d.将其中的"test"替换为"exam"  str.replace()

# a.统计该字符串中字母s出现的次数

str1 = 'this is a test of Python'
count = 0
for ch in str1:
    if ch == 's':
        count += 1
print(count)

# b.取出子字符串“test”   str.find('test')
str1 = 'this is a test of Python'
start = str1.find('test')
end = start + len('test')
print(str1[start:end])

# c.采用不同的方式将字符串倒序输出
str1 = 'this is a test of Python'
print(str1[::-1])

str2 = ""
for i in range(len(str1)-1, -1, -1):
    str2 += str1[i]
print(str2)

# d.将其中的"test"替换为"exam"  str.replace()
str1 = 'this is a test of Python'
str2 = str1.replace('test', 'exam')
print(str2)


# 2.已知字符串 a = "aAsmr3idd4bgs7Dlsf9eAF",要求如下
# 	a.请将a字符串的大写改为小写，小写改为大写 ch.lower()小写， ch.upper()大写
# 	b.请将a字符串的数字取出，并输出成一个新的字符串 ch>='0' and ch<='9'
# 	c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
# 	    并输出成一个字典。 例 {'a':4,'b':2}
# 	d.输出a字符串出现频率最高的字母
# 	e.请判断'boy'里出现的每一个字母，是否都出现在a字符串里。
# 	    如果出现，则输出True，否则，则输 出False

# a.请将a字符串的大写改为小写，小写改为大写 ch.lower()小写， ch.upper()大写
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = ""
for ch in a:
    if ch>='a' and ch<='z':
        b += ch.upper()
    elif ch>='A' and ch<='Z':
        b += ch.lower()
    else:
        b += ch
print(b)  # AaSMR3IDD4BGS7dLSF9Eaf

# b.请将a字符串的数字取出，并输出成一个新的字符串 ch>='0' and ch<='9'
a = "aAsmr3idd4bgs7Dlsf9eAF"
b = ''
for ch in a:
    if ch>='0' and ch<='9':
        b += ch
print(b)  # "3479"

# c.请统计a字符串出现的每个字母的出现次数（忽略大小写，a与A是同一个字母），
# 	 并输出成一个字典。 例 {'a':4,'b':2}
a = "aAsmr3idd4bgs7Dlsf9eAF"
a = a.lower()

dic = {}
for ch in a:
    if ch>='a' and ch<='z':
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
print(dic)
# {'a': 3, 's': 3, 'm': 1, 'r': 1, 'i': 1, 'd': 3, 'b': 1, 'g': 1, 'l': 1, 'f': 2, 'e': 1}

# d.输出a字符串出现频率最高的字母
max_num = 0
for v in dic.values():
    if v > max_num:
        max_num = v
# print(max_num)  # 3

for k, v in dic.items():
    if v == max_num:
        print(k, end=', ')
print()


# 注：能不使用系统功能的尽量不要使用，自己实现
# 中级
# 1.去除字符串两端的指定字符.
str1 = 'hhelhlohh'
ch = 'h'

i = 0
while i < len(str1):
    if i==0 and str1[i] == ch:
        str1 = str1[1:]
        i -= 1
    else:
        break
    i += 1

i = len(str1)-1
while i >= 0:
    if i==len(str1)-1 and str1[i]==ch:
        str1 = str1[:-1]
    i -= 1

print(str1)


# 2.键盘输入一句英文 将每个单词的首字母大写
# 	例如:
# 		输入: hello nice to meet you
# 		转化之后: Hello Nice To Meet You
str1 = 'hello nice to meet you'
str2 = ''
for i in range(len(str1)):
    if i==0 or str1[i-1]==' ':
        str2 += str1[i].upper()
    else:
        str2 += str1[i]
print(str2)


# 3.输入一个字符串，压缩字符串如下aabbbccccd变成a2b3c4d1
str1 = "aabbbccccd"
dic = {}
for ch in str1:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1
print(dic)
# {'a': 2, 'b': 3, 'c': 4, 'd': 1}

str2 = ""
for k, v in dic.items():
    str2 += k + str(v)

print(str2)  # a2b3c4d1


str1 = "aabbbccccd"
str2 = ''
count = 0
for i in range(len(str1)):
    if i == 0:
        str2 += str1[i]
        count = 1
    elif str1[i] == str1[i-1]:
        count += 1
    else:
        str2 += str(count)
        str2 += str1[i]
        count = 1

str2 += str(count)

print(str2)


# 4.完成猜拳游戏
# 		-----------------------------
# 		请输入你的选择:
# 		1. 石头
# 		2. 剪刀
# 		3. 布
# 		-----------------------------
# 		你的选择是【布】, 电脑的选择是【石头】
# 		恭喜你获得了胜利！
#

print('''-----------------------------
    请输入你的选择:
    1. 石头
    2. 剪刀
    3. 布
-----------------------------''')

while True:
    me = int(input("请猜拳(输入编号):"))
    computer = random.choice([1,2,3])
    print(me, computer)

    if me-computer==-1 or me-computer==2:
        print("恭喜你获得了胜利！")
        break
    elif me == computer:
        print("平手")
    else:
        print("我输了")