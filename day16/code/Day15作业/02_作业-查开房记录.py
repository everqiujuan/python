
#
# 题目： 开房查询
# 	创建函数，传入一个名字，查找到这哥们所有的开房记录，
#            然后写入到以这哥们名字为名的txt文件中 如：张三.txt
#
# 孙旸,310104198405232812,M,19840523,上海市瑞金二路129弄6号,-,13764090424,-,-,gemini9991@gmail.com,


def fn(name):

    fp = open("kaifanglist.txt", "r", encoding='utf-8')
    content_list = fp.readlines()
    fp.close()

    info_list = []
    for content in content_list:
        line_list = content.split(",")
        if len(line_list) > 1:
            if name == line_list[0]:
                info_list.append(content)
    # print(info_list)

    # 写
    fp2 = open(name + ".txt", 'w', encoding='utf-8')
    info = "".join(info_list)
    fp2.write(info)
    fp2.close()


fn("周建华")
