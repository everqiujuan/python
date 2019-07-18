
# 算术运算符
#  四则运算： +, -, *, /
#  % 取余， **次方， // 取整

print(1 + 1)
print(10 - 5)
print(3 * 4)
print(10 / 3)  # 浮点数精度问题
print(10 % 3)  # 1
print(2 ** 10)
print(10 // 3)  # 3


# 比较运算符
#  >, >=, <, <=, ==, !=
print(3 > 4)  # False
print(3 >= 3)  # True
print(3 < 4)  # True
print(3 <= 4)  # True
print(3 == 3)  # True
print(3 == '3')  # False
print(3 != 3)  # False

# 字符串比较
# ASCII码
# 0-9 ： 48-57
# a-z : 97-122
# A-Z : 65-90
print('a' > 'b')  # False
print('c' >= 'b')  # True
print('abcd' < 'abca')  # False
# print('a' > 32)  # 不同类型不能比较，报错

# 判断某个字符是否为大写字母
ch = 'D'
print(ch >= 'A' and ch <= 'Z')  # True


