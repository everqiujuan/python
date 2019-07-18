
import os

# 文件文件的绝对路径
# Y:\python1807\Python\day11\code\05_os模块2.py
print(os.path.abspath('05_os模块2.py'))

# 拼接路径 【掌握】
print(os.path.join(r'Y:\python1807\Python\day11\code', 'hello.py'))
# Y:\python1807\Python\day11\code\hello.py

# 拆分
print(os.path.split(r'Y:\python1807\Python\day11\code\hello.py'))
# ('Y:\\python1807\\Python\\day11\\code', 'hello.py')

# 拆分文件名
print(os.path.splitext('hello.py'))
# ('hello', '.py')


dir1 = r'Y:\python1807\Python\day11\code'
file1 = r'Y:\python1807\Python\day11\code\05_os模块2.py'

# isdir() : 判断是否为文件夹 【掌握】
print(os.path.isdir(dir1))  # True
print(os.path.isdir(file1))  # False

# isfile(): 判断是否为文件【掌握】
print(os.path.isfile(dir1))  # False
print(os.path.isfile(file1))  # True

# exists() : 判断是否存在【掌握】
print(os.path.exists(dir1))  # True
print(os.path.exists(file1))  # True


# getsize(): 获取文件的大小 【掌握】
print(os.path.getsize(file1))  # 996

# dirname(): 父目录 【掌握】
print(os.path.dirname(file1))  # Y:\python1807\Python\day11\code

# basename(): 文件名
print(os.path.basename(file1))  # 05_os模块2.py


# dir(): 获取指定文件的所有内容（属性或方法名）
import math
print(dir(math))



