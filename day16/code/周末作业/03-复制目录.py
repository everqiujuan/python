
# 复制目录（考虑拷贝所有子文件）
import os

def copyPath(sourcePath, targetPath):

    # 判断原目录是否存在
    if not os.path.exists(sourcePath):
        return "目录不存在"
    # 判断目标目录是否存在，如果不存在则创建
    if not os.path.exists(targetPath):
        os.mkdir(targetPath)

    filenameList = os.listdir(sourcePath)
    for filename in filenameList:
        absPath = os.path.join(sourcePath, filename)  # 源文件的子文件路径或子目录路径
        absPath2 = os.path.join(targetPath, filename)  # 目标文件的子文件路径或子目录路径

        if os.path.isfile(absPath):
            copy_file(absPath, absPath2)
        else:
            copyPath(absPath, absPath2)

    # 提示：
    # 遍历sourcePath下的所有子目录和子文件
    #   1， 如果是子文件，则复制文件
    #   2， 如果是子目录，在目标目录创建相同的目录名称，递归调用
    #  注意：子文件或子目录的绝对路径

def copy_file(sourcePath, targetPath):

    fp1 = open(sourcePath, 'rb')
    fp2 = open(targetPath, 'ab')

    # 大文件
    while True:
        content = fp1.read(1024)
        if len(content) == 0:  # 写完了
            break
        fp2.write(content)
        fp2.flush()  # 清空缓冲区

    fp1.close()
    fp2.close()



if __name__ == "__main__":
    # 将sourcePath目录的所有内容拷贝到targetPath目录下
    sourcePath = r"Y:\python1807\Python\day15"
    targetPath = r"Y:\python1807\Python\day15666"
    copyPath(sourcePath, targetPath)