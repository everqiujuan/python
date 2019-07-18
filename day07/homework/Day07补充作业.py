

# 1,将下面的字符串str1的敏感字符*都去掉:
#     然后再将str1的空格都去掉;
#      str1 = "H e  l  ** l    o    Wo r         L d  !"
str1 = "H e  l  ** l    o    Wo r         L d  !"


# 2,去掉字符串123@zh@qq.com中的@;
str2 = "123@zh@qq.com"



# 3, 任意给定的一串字符，统计字符串里面的大写字母和小写字母的个数
#   如： str1 = "HelloWorLD123"
str3 = "HelloWorLD123"



# 4, 获取网址中指定参数的值: https://www.baidu.com/s?name=avery&age=20&sex=male
#   如：参数param="name" 则结果为avery，
#   如：参数param="age" 则结果为20，
#   如：参数param="sex" 则结果为male，
urlStr = "https://www.baidu.com/s?name=avery&age=20&sex=male"
param = 'name'
# split()
# 1，按照?拆分=> ['https://www.baidu.com/s', 'name=avery&age=20&sex=male']
# 2, 将'name=avery&age=20&sex=male'按照&拆分 =>['name=avery', 'age=20', sex=male]
# 3, for 遍历 ['name=avery', 'age=20', sex=male]
#       将'name=avery'按照=拆分 => ['name', 'avery']


# https://www.baidu.com/s?name=avery&age=20&sex=male
# https:// : 协议
# www.baidu.com：域名(内部是ip地址)
# /s : 路径
# ? 分隔服务器地址和参数部分
# name=avery&age=20&sex=male： 参数部分，不同参数使用&符号隔开， 每个参数的格式: name=avery



# 5,将字符串按照单词进行逆序，空格作为划分单词的唯一条件
#      如传入:”Welome to Beijing”改为 “Beijing to Welcome”



# 6,查找子串出现的次数，返回字符串str中出现子串的次数
#      如传入:”abcabcabc”, “abc”;  返回:3
#          “ababacccababa”, “aba”, 返回：2,  如果返回4呢



# 7,将字符中单词用空格隔开
#       已知传入的字符串中只有字母,每个单词的首字母大写，
#       请将每个单词用空格隔开，只保留第一个单词的首字母大写
#       传入:”HelloMyWorld”
#       返回:”Hello my world”









