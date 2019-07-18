

#
# 正则表达式 : Regular Expression
#   作用：匹配指定规则的字符串
# 爬虫，匹配手机号，邮箱，qq号等
#

# 验证手机号码是否为11位，且第一位是1，都为数字
def fn(phone):
    if len(phone) != 11:
        return False
    if phone[0] != '1':
        return False
    if not phone.isdigit():
        return False
    return True

fn("13456788765")


# 使用正则表达式
import re

# re.match(): 匹配字符串是否以指定正则表达式开头，类似字符串中的startswith, 如果能够匹配成功则返回对象, 否则返回None
#   参数1： 正则表达式
#   参数2： 需要匹配的字符串
#   参数3： 标记
#             re.I : ignore,忽略大小写
#             re.M : 换行模式
#             re.S : 跟符号.配合使用，让.可以匹配到换行
# res = re.match('www', 'www.baidu.com')
# res = re.match('www', 'ww.baidu.www.com')
# res = re.match('www', 'WWW.baidu.com', re.I)
# print(res)


# re.search(): 匹配字符串中是否出现指定正则表达式的内容，如果有则返回第一次匹配到的内容，否则返回None
# res = re.search("www", 'www.baidu.com')
# res = re.search("www", 'baidu.www.com')
# res = re.search("www", 'baidu.wwww.www.com')
# res = re.search("www", 'baidu.WWWW.www.com', re.I)
# res = re.search("www", 'w.baidu.com')  # None
# print(res)


# re.findall(): 获取字符串中匹配正则表达式的所有内容，如果没有匹配的则返回空列表
# res = re.findall('www', 'www.baidu.com')  # ['www']
# res = re.findall('www', 'www.baidu.WWw.com', re.I)  # ['www', 'WWw']
res = re.findall('www', 'w.baidu.Ww.com')  # []
print(res)











