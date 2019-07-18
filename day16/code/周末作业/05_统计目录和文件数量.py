
# 1、使用函数递归，分别统计文件夹newdir中文件和文件夹的个数
#    提示：统计当前目录下的文件数量和文件夹数量
#         如果碰到文件，则文件数量+1
#         如果碰到文件夹，则文件夹数量+1，递归调用fn()并传入当前子文件夹目录，

import os

# file_count = 0
# dir_count = 0
# def fn(dirPath):
#
#     filenameList = os.listdir(dirPath)
#     for filename in filenameList:
#         absPath = os.path.join(dirPath, filename)
#
#         if os.path.isfile(absPath):
#             global file_count
#             file_count += 1
#         else:
#             global dir_count
#             dir_count += 1
#             fn(absPath)


# def fn(dirPath, countList):
#     filenameList = os.listdir(dirPath)
#     for filename in filenameList:
#         absPath = os.path.join(dirPath, filename)
#
#         if os.path.isfile(absPath):
#             countList[0] += 1
#         else:
#             countList[1] += 1
#             fn(absPath, countList)
#
# if __name__ == '__main__':
#     countList = [0, 0]
#     fn(r"Y:\python1807\Python\day16\code\周末作业\newdir", countList)
#     print(countList)


def fn(dirPath):

    file_count = 0
    dir_count = 0

    filenameList = os.listdir(dirPath)
    for filename in filenameList:
        absPath = os.path.join(dirPath, filename)

        if os.path.isfile(absPath):
            file_count += 1
        else:
            dir_count += 1
            f_count, d_count = fn(absPath)
            file_count += f_count
            dir_count += d_count

    return file_count, dir_count


if __name__ == '__main__':
    res = fn(r"Y:\python1807\Python\day16\code\周末作业\newdir")
    print(res)
