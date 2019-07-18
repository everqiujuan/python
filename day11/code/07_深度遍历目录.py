
# 深度遍历(了解)
# 栈：后进先出

import os

# 遍历目录
def getAllDirAndFile(sourcePath):

    # 创建栈
    stack = []  # []
    stack.append(sourcePath)  # [newdir]

    while True:

        if len(stack) == 0:
            break

        # 从栈的右边取文件名
        dirPath = stack.pop()  # []

        # 获取sourcePath所有子文件夹和子文件名称
        filenameList = os.listdir(dirPath)
        for filename in filenameList:
            absPath = os.path.join(dirPath, filename)

            # 文件
            if os.path.isfile(absPath):
                print('文件名:', filename)
            # 目录
            elif os.path.isdir(absPath):
                stack.append(absPath)
                print('目录:', filename)

    #  [newdir]
    #  newdir [dir1, dir2, dir3]
    #  dir3 [dir1, dir2, dir3-1]
    #  dir3-1 [dir1, dir2]
    #  dir2 [dir1]
    #  dir1 [dir1-1, dir1-2]
    #  dir1-2 [dir1-1]
    #  dir1-1 []

path = r'Y:\python1807\Python\day11\code\newdir'
getAllDirAndFile(path)



print("-----递归的方式遍历-----")
# 深度遍历（递归） 【掌握】
def get_all_dir_and_file(sourcePath):

    filenameList = os.listdir(sourcePath)
    for filename in filenameList:
        absPath = os.path.join(sourcePath, filename)

        # 文件
        if os.path.isfile(absPath):
            print('文件名:', filename)
        # 目录
        elif os.path.isdir(absPath):
            print('目录:', filename)

            # 递归遍历子目录
            get_all_dir_and_file(absPath)

path = r'Y:\python1807\Python\day11\code\newdir'
get_all_dir_and_file(path)



