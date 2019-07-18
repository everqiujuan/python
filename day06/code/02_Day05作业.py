#
# 初级
# 【注：以下6题功能全部自己实现，不能借助于Python内置函数】
# 1.自定义一个数字列表，获取这个列表中的最小值，并将列表转化为元组
list1 = [2, 3, 1, 5, 6, -7, 4]
m = list1[0]
for n in list1:
    if n < m:
        m = n
print(m)
print(tuple(list1))

# 2.自定义一个数字列表，元素为10个 ,找出列表中最大数连同下标一起输出
list1 = [2, 3, 1, 5, 6, -7, 4]
m = list1[0]
index = 0
for i in range(len(list1)):
    if list1[i] > m:
        m = list1[i]
        index = i

print(m, index)

# 3 .自定义一个数字列表，求列表中第二大数的下标
list1 = [2, 3, 1, 5, 6, -7, 4]

max1 = list1[0]
for n in list1:
    if n > max1:
        max1 = n
print(max1)

max2 = list1[0]
index2 = 0
for i in range(len(list1)):
    if list1[i] > max2 and list1[i] != max1:
        max2 = list1[i]
        index2 = i
print(max2, index2)


# 4.B哥去参加青年歌手大奖赛 ,有10个评委打分 ,(去掉一个最高分一个最低分)求平均分
list1 = [2, 3, 1, 5, 6, -7, 4]
max1 = list1[0]  # 最大数
min1 = list1[0]  # 最小数
for n in list1:
    if n > max1:
        max1 = n
    if n < min1:
        min1 = n

list1.remove(max1)
list1.remove(min1)

s = 0
for n in list1:
    s += n

print(s / len(list1))


# 5 .定义元组，存放5个学生的成绩【成绩值自己设定】，获得成绩之和，平均成绩，最小成绩，最大成绩。
scores = (99, 98, 60, 59, 80, 40)
s = 0
max1 = scores[0]
min1 = scores[0]
for n in scores:
    s += n
    if n > max1:
        max1 = n
    if n < min1:
        min1 = n
avg = s / len(scores)

print("成绩和：", s)
print("平均成绩：", round(avg, 2))
print("最高成绩：", max1)
print("最低成绩：", min1)


# 6 .将一个列表逆序输出
list1 = [99, 98, 60, 59, 80, 40]
list2 = []
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
print(list2)
# list2 = list1[::-1]


# 中级
# 1.给定一个列表：将列表中指定的某个元素全部删除
list1 = [1,4,3,4,4,4,4,2]
n = 4
for i in range(list1.count(n)):
    list1.remove(n)
print(list1)

# 2.自定义一个列表，最大的与第一个元素交换，最小的与最后一个元素交换，输出列表
list1 = [0,4,5,6,1,3,7,2]
maxIndex = 0
minIndex = 0
for i in range(len(list1)):
    if list1[i] > list1[maxIndex]:
        maxIndex = i
    if list1[i] < list1[minIndex]:
        minIndex = i
list1[0], list1[maxIndex] = list1[maxIndex], list1[0]
if minIndex == 0:
    minIndex = maxIndex
list1[-1], list1[minIndex] = list1[minIndex], list1[-1]

print(list1)


# 3.在控制台输入一句英语，获得每个字母出现的次数，注：每个字符作为key，出现的次数作为value生成一个字典
str1 = "hello boy"
dic = {}
for ch in str1:
    if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1

    # {'h': 1, 'e':1, 'l': 2, 'o':1...}
print(dic)

# 4 ,对称列表. 传入一个列表，元素类型与个数皆未知，返回新列表，由原列表的元素正序反序拼接而成;
# 如传入[“One”, “Two” ,”Three”] 返回[“One”, “Two”, “Three” ,”Three” ,”Two”, “One”]
list1 = ['One', 'Two', 'Three']
list2 = list1 * 1
list2.reverse()
list3 = list1 + list2
print(list3)

# 5 ,给定一个不存在重复元素的整数列表，例如[6 ,4 ,7 ,2 ,5 ,8]和一个数字，例如10，
# 找出两个元素(或同一个元素加自身)，并且使这两个数的和为给定数字，并打印出来
# 例如[6 ,4 ,7 ,2 ,5 ,8]和数字10. 打印结果为: 6 ,4  2 ,8  5 ,5
list1 = [6 ,4 ,7 ,2 ,5 ,8]
n = 10
for i in range(len(list1)):
    for j in range(i, len(list1)):
        if list1[i] + list1[j] == n:
            print(list1[i], list1[j])


# 6 ,有一个从小到大排好序的列表。现输入一个数，要求按原来的规律将它插入列表中,
# 如: [2 ,3 ,4 ,56 ,67 ,98]    / /如插入63, 100
list1 = [2 ,3 ,4 ,56, 67 ,98]
n = 100
for i in range(len(list1)):
    if n < list1[i]:
        list1.insert(i, n)
        break
else:
    list1.append(n)

print(list1)

# 7 ,列表去重, 将下面的列表中重复的元素去除
# list1 = [1 ,2 ,3 ,5 ,4 ,4 ,4 ,5 ,5 ,3 ,2 ,1]
# 方式一:
list1 = [1 ,2 ,3 ,5 ,4 ,4 ,4 ,5 ,5 ,3 ,2 ,1]
list2 = []
for n in list1:
    if n not in list2:
        list2.append(n)
print(list2)

# 方式二：
list1 = [1 ,2 ,3 ,5 ,4 ,4 ,4 ,5 ,5 ,3 ,2 ,1]
i = 0
while i < len(list1):

    j = i+1
    while j < len(list1):
        if list1[i] == list1[j]:
            list1.pop(j)
            j -= 1
        j += 1

    i += 1

print(list1)

# 方式三：
list1 = [1 ,2 ,3 ,5 ,4 ,4 ,4 ,5 ,5 ,3 ,2 ,1]
dic = {}
for n in list1:
    dic[n] = 0

list2 = list(dic.keys())
print(list2)





