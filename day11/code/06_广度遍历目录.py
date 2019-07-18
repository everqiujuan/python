
# 遍历目录（了解）
# 广度遍历： 使用队列


# 遍历newdir目录下的所有文件和目录
# 队列：先进先出
# 1遍历newdir子目录:
#   输出：dir1,dir2,dir3,test1.txt,test2.txt
#   队列：[dir1,dir2,dir3]
# 2遍历dir1子目录:
#   输出： dir1-1,dir1-2
#   队列：[dir2,dir3,dir1-1,dir1-2]
# 3遍历dir2子目录:
#   输出： test3.txt
#   队列：[dir3,dir1-1,dir1-2]
# 4遍历dir3子目录:
#   输出：dir3-1
#   队列：[dir1-1,dir1-2，dir3-1]
# 5遍历dir1-1:
#   输出：test5.txt
#   队列：[dir1-2,dir3-1]
# 6遍历dir1-2:
#   输出： test6.txt
#   队列：[dir3-1]
# 7遍历dir3-1:
#   输出：test4.txt
#   队列：[]


import os
import collections


# 遍历目录
def getAllDirAndFile(sourcePath):

    # 创建队列
    queue = collections.deque()  # []
    queue.append(sourcePath)  # [newdir]

    while True:

        if len(queue) == 0:
            break

        # 从队列的左边取文件名
        dirPath = queue.popleft()  # []

        # 获取sourcePath所有子文件夹和子文件名称
        filenameList = os.listdir(dirPath)
        for filename in filenameList:
            absPath = os.path.join(dirPath, filename)
            # dirPath: 'Y:\python1807\Python\day11\code\newdir'
            # filename: dir1

            # 文件
            if os.path.isfile(absPath):
                print('文件名:', filename)
            # 目录
            elif os.path.isdir(absPath):
                queue.append(absPath)
                print('目录:', filename)


path = r'Y:\python1807\Python\day11\code\newdir'
getAllDirAndFile(path)


