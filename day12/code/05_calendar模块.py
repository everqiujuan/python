
''''''
'''
calendar(year,w=2,l=1,c=6)  
   打印某一年的日历【c间隔距离; w每日宽度间隔; l是每星期行数 】
isleap(year)   判断是否是闰年
leapdays(y1, y2)  [y1, y2) 中间闰年的个数
month(year,month,w=2,l=1)  打印指定月份的日历
monthcalendar(year,month)  
   返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
   Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
monthrange(year,month)  
   返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。
   日从0（星期一）到6（星期日）;月从1到12。
'''

import calendar
c = calendar.calendar(2018, w=2, l=1, c=6)
# print(c)

print(calendar.isleap(2018))  # False
print(calendar.leapdays(1000, 2000))  # 242
m = calendar.month(2018, 7, w=2, l=1)
print(m)
print(calendar.monthcalendar(2018, 7))
print(calendar.monthrange(2018, 7))


