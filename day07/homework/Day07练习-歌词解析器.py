﻿
"""[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""



import time

musicLrcStr = """[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
"""

# 按照歌词时间，每隔1秒显示下句歌词
# time.sleep(1)  # 暂停1秒

# 1， 按行拆分， 得到每一行歌词， 如：lineStr = '[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼'
# 2， 将每一行歌词按照']'拆分，得到列表，
#       如 lineList = ['[04:40.75', '[02:39.90', '[00:36.25', '只是因为在人群中多看了你一眼']
# 3,  将歌词内容， 和歌词时间分别取出, 可以使用字典来保存歌词时间和对应的歌词内容
#               lrcDict = {}
#       歌词内容 lrcContent = lineList.pop()  # '只是因为在人群中多看了你一眼'
#               lineList变成： ['[04:40.75', '[02:39.90', '[00:36.25']
#       歌词时间 for lrcTime in lineList:
#                   lrcTime2 = lrcTime[1:]
#                   lrcDict[lrcTime2] = lrcContent
#
#           # 歌词内容就会按以下方式存储
#           # lrcDict = {'04:40.75': '只是因为在人群中多看了你一眼',
#                        '02:39.90': '只是因为在人群中多看了你一眼',
#                        '00:36.25': '只是因为在人群中多看了你一眼'
#                       }
#
#           注意歌词时间需要转换成秒，如：lrcDict[lrcTime] = lrcContent
#
# 4, 将lrcDict中的lrcTime全部取出存放在列表中，将列表升序排序，、
# 5，最后遍历列表， 每隔1秒 按照歌词的时间取出对应的歌词内容
#











