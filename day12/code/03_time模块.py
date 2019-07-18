

# UTC: 国际时间，格林尼治时间，格林尼治是英国伦敦的一个郊区
#      从1970年1月1号0点开始到指定时间的时间戳
# 夏令时
# 时间戳：从1970年1月1号0点开始到指定时间的秒数
#
# 时间的表现形式
#    时间戳：1533002305.981
#    时间元组：
#           tm_year: 年
#           tm_mon： 月（1~12）
#           tm_mday：天（1~31）
#           tm_hour：时（0~23）
#           tm_min：分（0~59）
#           tm_sec：秒（0~59）
#           tm_wday: 一周中的第几天（0~6，0表示星期一）
#           tm_yday：一年中的第几天（1~366）
#           tm_isdst：是否是夏令时
#
#    时间字符串：
#

import time

# time(): 获取当前时间的时间戳 timestamp
t = time.time()  # 【掌握】
print(t)  # 1533002305.981

# gmtime(): 时间戳 -> 时间元组，UTC时间
# print(time.gmtime())  # 默认是获取当前时间的时间元组
print(time.gmtime(t))
# time.struct_time(
#   tm_year=2018, tm_mon=7, tm_mday=31,
#   tm_hour=2, tm_min=3, tm_sec=49,
#   tm_wday=1, tm_yday=212, tm_isdst=0
#  )

# localtime(): 时间戳 -> 时间元组，中国标准时间
# print(time.localtime())
t2 = time.localtime(t)
print(t2)
print(t2[0])  # 2018
print(t2[1])  # 7
# time.struct_time(
#       tm_year=2018, tm_mon=7, tm_mday=31,
#       tm_hour=10, tm_min=7, tm_sec=22,
#       tm_wday=1, tm_yday=212, tm_isdst=0
# )

# mktime() : 时间元组 -> 时间戳
print(time.mktime(t2))  # 1533004246.0


#
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00-59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %% %号本身

# strftime() : 时间元组 -> 时间字符串
t = time.localtime()
str1 = time.strftime("%Y-%m-%d %H:%M:%S", t)  # "2018-07-31 10:36:44"
str1 = time.strftime("%y/%m/%d", t)  # "18/07/31"
str1 = time.strftime("%x %X", t)  # "07/31/18 10:38:35"
str1 = time.strftime("%j", t)  # "212"
# str1 = time.strftime("%Y年%m月%d日", t)  # 报错
str1 = time.strftime("%Y{y}%m{m}%d{d}", t).format(y="年", m='月', d='日')  # 报错
print(str1)  # 2018年07月31日

# format()
# print("hello{name}".format(name='张三'))  # hello张三

# 时间字符串 -> 时间元组
str1 = "2018-11-11 03:08:11"
t2 = time.strptime(str1, "%Y-%m-%d %I:%M:%S")
print(t2)

# 时间元组 -> 时间字符串, 格式固定
print(time.asctime(time.localtime()))  # "Tue Jul 31 10:51:11 2018"

# 时间戳 -> 时间字符串
print(time.ctime(time.time()))  # "Tue Jul 31 10:52:47 2018"


# sleep()  # 暂停
for i in range(2):
    time.sleep(1)
    print(i)


# 检测运行时间
# clock():
start = time.clock()
print(start)  # 5e-07, 接近0

time.sleep(2)  # 【掌握】

end = time.clock()
print(end)  # 1.9999233， 接近2

time.sleep(3)

print(time.clock())  # 5.0000127

# 科学计数法
# 5e-07 = 5 * 10^-7 = 0.0000005

