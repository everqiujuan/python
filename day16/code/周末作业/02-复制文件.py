

# 1、拷贝文件【考虑大文件拷贝，每次读取1024字节拷贝】


def copy_file(sourcePath, targetPath):

    fp1 = open(sourcePath, 'rb')
    fp2 = open(targetPath, 'ab')

    # content = fp1.read()
    # fp2.write(content)

    # 大文件
    while True:
        content = fp1.read(1024)
        if len(content) == 0:  # 写完了
            break
        fp2.write(content)
        fp2.flush()  # 清空缓冲区

    fp1.close()
    fp2.close()


if __name__ == '__main__':
    sourcePath = r"Y:\python1807\Python\day16\code\周末作业\01-递归删除文件夹.py"
    targetPath = r"Y:\python1807\Python\day16\code\周末作业\01-递归删除文件夹-副本.py"

    copy_file(sourcePath, targetPath)

