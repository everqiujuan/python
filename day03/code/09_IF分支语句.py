

# 分支语句
# If : 如果

# 程序 3大基本结构
#   1，顺序结构
#   2，分支结构
#   3，循环结构

# If单分支
age = int(input('请输入您的年纪:'))
if age >= 18:
    print('你成年了，可以去网吧吃鸡了')
    print('还可以玩王者荣耀')


# If双分支
# if - else
if age > 60:
    print('你是老男人了')
else:
    print("你还年轻")


# If多分支
# if - elif - elif..- else
if age < 18:
    print("你还是未成年人")
elif age < 40:
    print("你是年轻人")
elif age < 60:
    print("你是中年人")
else:
    print("你是老年人")


# If嵌套
# 2.从控制台输入三个数，输出较大的值，不能使用max()
a = int(input('请输入a的值:'))
b = int(input('请输入b的值:'))
c = int(input('请输入c的值:'))

if a > b:
    if a > c:
        print("最大值是:", a)
    else:
        print("最大值是:", c)

else:
    if b > c:
        print("最大值是:", b)
    else:
        print("最大值是:", c)

# 方法二
m = a
if b > a:
    m = b
if c > m:
    m = c
print(m)


# 随机数
import random
n = random.randrange(10, 100)  # 随机取[10, 100)的整数
print(n)

