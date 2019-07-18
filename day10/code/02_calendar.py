
# 万年历
# b 判断是否为闰年
def is_leap(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    return False

# C 某月的总天数
def get_mon_days(year, month):
    days = 31
    if month == 2:
        if is_leap(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    return days

# D year年份举例1900年1月1日的总天数
def get_year_days(year):
    days = 0
    for y in range(1900, year):
        if is_leap(y):
            days += 366
        else:
            days += 365
    return days

# E 第year年当前月份举例1月1号的总天数
def get_year_mon_days(year, month):
    days = 0
    for m in range(1, month):
        days += get_mon_days(year, m)
    return days

# F 计算1900年到当前月份的天数
def get_days(year, month):
    return get_year_days(year) + get_year_mon_days(year, month)

# G 计算当前月第一天的星期
def get_week(year, month):
    return (get_days(year, month)+1) % 7


# 主函数
def main():
    year = int(input("输入年:"))
    month = int(input("输入月:"))


    week = get_week(year, month)
    print('星期', week)

    print("星期日\t星期一\t星期二\t星期三\t星期四\t星期五\t星期六\t")

    # 当前月的总天数
    days = get_mon_days(year, month)
    for i in range(week):
        print(" ", end="\t\t")

    for d in range(1, days+1):
        print(d, end='\t\t')
        if (week+d)%7 == 0:
            print()

main()