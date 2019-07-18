
#
# 题目：创建函数， 从文件guishudi.txt中获取数据，输入完整手机号11位，匹配前7位，输出对应的地址和卡类型
#
# 60268|1340475|0431|吉林省长春市|吉林移动大众卡
#   手机号前7位 ：1340475
#

def fn(phone):
    phone = phone[:7]

    fp = open("guishudi.txt", "r", encoding='utf-8')
    content_list = fp.readlines()
    fp.close()

    for content in content_list:
        line_list = content.split("|")
        if len(line_list) >= 5:
            if line_list[1] == phone:
                return line_list[3], line_list[4]


res = fn("15815841234")
print(res)


# 文件操作：
#   1，打开文件
#   2，读,写
#   3，关闭文件











