
# os: 操作系统 operate system
# os模块：主要提供系统相关的操作
import os

# 目录: dir，文件夹
# curdir: 获取当前文件所在目录
print(os.curdir)  # . 表示当前目录
                  # .. 表示上一层目录

# 绝对路径：从磁盘目录开始的完整路径
#   Y:\python1807\Python\day11\code\04_os模块1.py
# 相对路径：相对指定文件的路径，如：从工程目录开始
#   day11/code/04_os模块1.py

# 获取当前目录
print(os.getcwd())  # Y:\python1807\Python\day11\code

# 【掌握】
# listdir(): 获取指定目录下的所有子文件夹或子文件的名称
print(os.listdir(r'Y:\python1807\Python\day11\code'))
# ['Thumbs.db', '03_Day10作业.py', '02_Day10-周末作业.py', 'newdir', '01_复习.py', '04_os模块1.py']

# mkdir(): 创建目录 【掌握】
# os.mkdir('情书')
# os.mkdir('情书.txt')  # 也是目录

# os.mkdir('c/c/c')
# os.makedirs('b/b/b')  #

# rmdir() 删除目录
# os.rmdir('c')

# rename(): 重命名文件夹或文件
# os.rename('情书', '遗书')
# os.rename('01_复习.py', '01_复习1.py')

# remove(): 删除文件
# os.remove('hello.txt')

# os.system('ipconfig')

# nt->windows
# posix -> Linux，mac
print(os.name)  # nt

# 环境变量
print(os.environ)
print(os.environ.get('PATH'))

# 文件属性
print(os.stat(r'Y:\python1807\Python\day11\code\04_os模块1.py'))

