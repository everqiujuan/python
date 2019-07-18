
# 使用协程爬取斗鱼妹子
# url = "https://www.douyu.com/gapi/rknc/directory/yzRec/3"


import requests
url='https://rpic.douyucdn.cn/live-cover/appCovers/2019/03/09/6523500_20190309142516_small.jpg'
res = requests.get(url)
with open('a.png', 'wb') as fp:
    fp.write(res.content)
