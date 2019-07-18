
import csv
import os

# csv 读取
def read_csv(filePath):
    if not os.path.isfile(filePath):
        return "文件不存在！"

    fp = open(filePath, 'r', encoding='utf-8')
    # print(fp.read())
    reader = csv.reader(fp)
    for line in reader:
        print(line)

    fp.close()


# csv 写
def write_csv(filePath):
    info_list = [["zhangsan", '33', '男'], ["zhangsan", '33', '男'], ["zhangsan", '33', '男']]
    # info_dict = {"name": "张三", 'age': 33}

    fp = open(filePath, 'w', encoding='utf-8', newline="")

    writer = csv.writer(fp)
    for info in info_list:
        writer.writerow(info)
    
    fp.close()

if __name__ == "__main__":
    # read_csv("text.csv")
    write_csv("text2.csv")
