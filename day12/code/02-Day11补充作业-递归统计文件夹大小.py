''''''

#
# 统计文件夹大小 (os.path.getSize()：获取文件大小)
#
import os

def fn(path):

    size = 0

    filenameList = os.listdir(path)
    for filename in filenameList:
        absPath = os.path.join(path, filename)

        # 文件
        if os.path.isfile(absPath):
            size += os.path.getsize(absPath)
        # 目录
        else:
            size += fn(absPath)

    return size

if __name__ == "__main__":
    res = fn(r"Y:\python1807\Python\day11")
    print(res)







