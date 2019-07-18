''''''
'''
dt_now = datetime.datetime.now()
        获取当前的日期对象，包含时间的
dt_ziding = datetime.datetime()
        根据指定的日期、时间生成一个日期对象
        
dt.strftime()  将日期对象转化为指定的格式
dt.date()   获取日期对象中的日期
dt.time()   获取日期对象中的时间
dt.timestamp()  获取日期对象的时间戳
dt.hour\minute\second  获取小时、分钟、秒

datetime.datetime.fromtimestamp()
        根据一个时间戳，转化为指定的日期对象
datetime.timedelta()
        生成一个差值对象，可以和日期对象直接进行相加减
        参数有，days,hours,minutes,seconds
'''

# 【掌握】
import datetime

# 获取当前日期对象
dt = datetime.datetime.now()
print(dt)  # 2018-07-31 11:04:54.394000
print(type(dt))  # <class 'datetime.datetime'>

# 获取指定日期的对象
dt = datetime.datetime(2019, 10, 10, 10, 11, 12, 111000)
print(dt)

print(dt.strftime("%Y-%m-%d"))  # "2019-10-10"
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour, dt.minute, dt.second)

print(dt.date())  # 2019-10-10
print(dt.time())  # 10:11:12.111000

# 时间戳
print(dt.timestamp())  # 1570673472.111

# 时间戳 -> 日期对象
print(datetime.datetime.fromtimestamp(1570673472.111))

# 时间差对象
dt_delta = datetime.timedelta(days=2, hours=3, minutes=4, seconds=5)
print(dt)
print(dt + dt_delta)

