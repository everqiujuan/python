
# for-in
# 语法格式：
#   for i in list:
#       print(i)
#

# 1+2+3+..+ 100
# range(100) : [0, 100)， 0-99
# range(1, 100): 1-99

# print(range(100))  # range(0, 100)

s = 0
for i in range(1, 101):  # 1-100
    # print(i)
    s += i

print(s)  # 5050

# 遍历列表 【重要】
list1 = [11, 22, 33, 44]
for n in list1:
    print(n)  # 元素

for i in range(len(list1)):  # range(4) => 0-3
    print(i)  # 下标
    print(list1[i])  # 值

# enumerate 枚举
for i, n in enumerate(list1):
    print(i, n)  # 下标, 元素



#
# 7, 一个新入职，月工资为2000元的员工，每年涨当年工资5%，20年后的月工资是多少？
# 第一年： 2000
# 第二年： 2000 + 2000*0.05
# 第三年： (2000 + 2000*0.05) + (2000 + 2000*0.05)*0.05
# 第四年： ((2000 + 2000*0.05) + (2000 + 2000*0.05)*0.05) + ((2000 + 2000*0.05) + (2000 + 2000*0.05)*0.05)*0.05
# ...
salary = 2000
for i in range(20):
    salary = salary + salary*0.05
print(salary)


# 8, 山上有一口缸可以装50升水，现在有15升水。老和尚叫小和尚下山挑水，每次可以挑5升。
#    问：小和尚要挑几次水才可以把水缸挑满？通过编程解决这个问题。
count = 0
i = 15
while i < 50:
    count += 1
    i += 5
print(count)  # 7


# 9, 打印100–200之间所有能被3或者7整除的数
for i in range(100, 201):
    if i%3==0 or i%7==0:
        print(i)


# 10, 计算10的阶乘   (1*2*3*4*5*6*7*8*9*10   n的阶乘1*2……*n)
n = 10
s = 1
for i in range(1, n+1):
    s *= i
print(s)  # 3628800


