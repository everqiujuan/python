
#
# 题目： 邮编查询
# 	创建函数， 传入一个邮编，得到归属地
#
# [513337,"四川省甘孜藏族自治州稻城县"],\n

def fn(postcode):

    fp = open("youbian.txt", 'r', encoding='utf-8')
    content_list = fp.readlines()
    fp.close()

    for content in content_list:
        line_str = content[:-2]
        line_list = eval(line_str)
        if line_list[0] == postcode:
            return line_list[1]

res = fn(513337)
print(res)
