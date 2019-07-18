''''''

# 递归删除文件夹(可能包含子文件或子文件夹)
# 【温馨提示：创建一个文件夹，不要直接操作已有的文件夹】

# 提示：要先将文件夹中的所有子文件删除再删除本文件夹
# remove(): 删除文件
# rmdir()： 删除空目录

import os

def fn(dirPath):

    filenameList = os.listdir(dirPath)

    for filename in filenameList:
        absPath = os.path.join(dirPath, filename)

        if os.path.isfile(absPath):
            os.remove(absPath)
        else:
            fn(absPath)

    os.rmdir(dirPath)

if __name__ == "__main__":
    fn(r"Y:\python1807\Python\day1555")



