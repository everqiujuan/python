
# 文件

try:
    fp = open("kaifanglist2.txt", 'r', encoding='utf-8')
    content = fp.read()
    print(content)

except BaseException as e:
    print("出现异常：", e)

else:
    fp.close()


# 简化
# with-as：可以不写fp.close()
with open('kaifanglist2.txt', 'r', encoding='utf-8') as fp:
    content = fp.read()
    print(content)






