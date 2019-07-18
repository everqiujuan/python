
import re

# 中文
chinesePattern = "[\u4e00-\u9fa5]+"
print(re.search(chinesePattern, "hello你好"))


# 匹配手机号: 11位，第一位是1，第二位3,4,5,7,8,9,第三位
# "^(13[0-9]|14[579]|15[0-35-9]|166|17[0135678]|18[0-9]|19[89])\d{8}$"
# pattern = "^(13[0-9]|14[579]|15[0-35-9]|166|17[0135678]|18[0-9]|19[89])\d{8}$"
pattern = "^1[3-9]\d{9}$"
print(re.search(pattern, "13422223333"))


# 匹配qq号： 5-11位, 第一位不能为0
pattern = "^[1-9]\d{4,10}$"
print(re.search(pattern, '5343422342'))


# 匹配任意一个邮箱  如：jack@163.com， 3333@qq.com, zhang@sina.com.cn
pattern = "^\w+@\w+\.\w+$"
print(re.search(pattern, 'jack@163.com'))


# 匹配身份证: 18位， 最后一位是数字或X
pattern = "^[1-9]\d{16}(\d|X)$"
print(re.search(pattern, "334454198811002233"))

# 邮政编码(共6位数字, 第一位不能为0)
pattern = "^[1-9]\d{5}$"
print(re.search(pattern, "518000"))


# 用户名(只能使用数字字母下划线, 且数字不能开头, 长度在6-15位)
pattern = "^[a-zA-Z_]\w{5,14}$"
print(re.search(pattern, "hello1"))


# 简单日期格式 如："2017-11-11"，"2017-1-1"
pattern = "^\d{4}-([1-9]|10|11|12)-\d{1,2}$"
print(re.search(pattern, "2017-11-11"))


# 图片文件格式 如："nbb.jpg", "aa.jpeg","aa.png", "aa.gif"
pattern = "^\w+\.(jpg|jpeg|png|gif)$"
print(re.search(pattern, "hello.jpg"))

