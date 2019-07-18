import time
import requests
import multiprocessing


# 模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

def get_page(page):
    url = 'https://sz.lianjia.com/ershoufang/pg%d/' % page
    response = requests.get(url, headers=headers)
    print('第%d页' % page, len(response.text))
    # print('第%d页' % page)


if __name__ == '__main__':

    start = time.time()

    p_list = []
    for i in range(1, 101):
        p = multiprocessing.Process(target=get_page, args=(i,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    end = time.time()
    print(end - start)



