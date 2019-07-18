

# 1.显示指定路径下所有视频格式文件：mp4，avi，rmvb
# filename.endswith('mp4')
import os


def fn(path):

    filenameList = os.listdir(path)

    for filename in filenameList:
        # 子文件或子目录的绝对路径
        absPath = os.path.join(path, filename)

        # 文件
        if os.path.isfile(absPath):
            if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.rmvb'):
                print(filename)
        # 目录
        elif os.path.isdir(absPath):
           fn(absPath)


if __name__ == "__main__":
    fn(r"Y:\python1807\Python\day12\code\dir")


# 2.自定义模块
# 	建立一个包
# 	在包的下创建一个排序的模块
# 	 	模块下的功能
# 			1. 使用冒泡排序对列表进行降序排序
# 			def fn(l):
#
# 			2. 使用选择排序对列表进行升序排序
#
# 			3. 查找列表的元素
# 				找到返回下标, 找不到返回-1
# 				def fn(l, n):
#
# 			4.使用顺序查询，获取列表中所有与指定元素重复的元素脚标
#                 def fn(l, n):
#
# 	在另外一个文件中导入上述包中的模块，完成模块中功能的调用

#
# 包：package, 就是一个文件夹，只是里面包含了一个__init__.py
#    方便代码管理，包还用于管理模块
# 模块：就是一个.py文件，需要遵守命名规范，封装代码
# 函数：封装功能
#       login()
#       register()


# 使用mymodule模块
# import mypackage.mymodule
from mypackage.mymodule import fn1, fn2, fn3, fn4

print(fn1([2,3,1,5]))

