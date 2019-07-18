
''''''

# 1,成绩判定
# 	大于85 优秀
# 	大于等于75小于等于85 良好
# 	大于等于60小于75 及格
# 	小于60  不及格
score = 90
if score > 85:
    print('优秀')
elif score >= 75:
    print('良好')
elif score >= 60:
    print("及格")
else:
    print('不及格')


# 2,判断一个年份是闰年还是平年；
# （1.能被4整除而不能被100整除.（如2004年就是闰年,1800年不是.）
#   2.能被400整除.（如2000年是闰年））
year = 2018
if year%4==0 and year%100!=0 or year%400==0:
    print("是闰年")
else:
    print("是平年")

# 3,输入一个月份，然后输出对应月份有多少天，将天数输出(不考虑闰年)
# 比如：
# 输入 6 输出为30
# 输入 2 输出为28
month = 7
if month == 2:
    print("28")
# elif month == 4 or month == 6 or month == 9 or month == 11:
elif month in [4,6,9,11]:
    print('30')
else:
    print("31")

# 4. 开发一款软件，根据公式（身高-108）*2=标准体重，可以有10斤左右的浮动。
# 来观察测试者体重是否合适, 输入真实身高，真实体重
height = 180
weight = 150
stadWeight = (height-108) * 2
if weight >= stadWeight-10 and weight <= stadWeight+10:
    print("合适")
else:
    print("不合适")

# 5, 入职薪水10K，每年涨幅入职薪水的5%，50年后工资多少？
salary = 10
result = salary + salary*0.05*50
print(result)

# 6, 为抵抗洪水，战士连续作战89小时，编程计算共多少天零多少小时？
hours = 89
day = hours // 24
hour = hours % 24
print(day,'天',hour,'时')

# 7, 给定一个5位数，分别把这个数字的万位， 千位，百位、十位、个位算出来并显示。如： 34567
n = 67876
a = n % 10
b = (n // 10) % 10
c = (n // 1000) % 10
d = n // 10000


# 8.分别输入某年某月某日，判断这一天是这一年的第几天？（考虑闰年） (*****)
# year, month， day
# 提示： 使用多个if单分支
year = 2018
month = 7
day = 19

days = day
if month > 1:
    days += 31
if month > 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days += 29
    else:
        days += 28
if month > 3:
    days += 31
if month > 4:
    days += 30
if month > 5:
    days += 31
if month > 6:
    days += 30
if month > 7:
    days += 31
if month > 8:
    days += 31
if month > 9:
    days += 30
if month > 10:
    days += 31
if month > 11:
    days += 30

print(days)


# 9,输入一个时间，输出该时间的下一秒： (*****)
# 	如：23:59:59， 输入：hour, min, sec
# 	输出 0: 0: 0
hour = 23
min = 59
sec = 59

sec += 1

if sec == 60:
    sec = 0
    min += 1

    if min == 60:
        min = 0
        hour += 1

        if hour == 24:
            hour = 0

print(hour, ":", min, ":", sec)

