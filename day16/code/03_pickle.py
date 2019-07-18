

# pickle模块
# 作用：
#   将Python对象(列表，字典，元组..) => 存入文件
#   存入文件的内容 => Python对象(列表，字典，元组..)

import pickle

# 将对象存入文件
names = ["杨玉环", '不知火舞', '貂蝉', '王昭君', '西施']
# names = {'name':'11', 'age':33}
fp = open("pickle.txt", 'wb')
pickle.dump(names, fp)  # 将names存入文件pickle.txt
fp.close()

# 将文件内容取出
fp2 = open('pickle.txt', 'rb')
res = pickle.load(fp2)
print(res)  # ['杨玉环', '不知火舞', '貂蝉', '王昭君', '西施']
print(type(res))  # <class 'list'>

# 数据持久化：存入硬盘，存文件
# 数据缓存：一般存入内存，临时存储
