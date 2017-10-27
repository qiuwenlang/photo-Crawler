# -*- coding:UTF-8 -*-
import requests
import os
import time

path = os.getcwd() + r'/huangbanwang'
os.mkdir(path)  # 创建文件夹
os.chdir(path)  # 改变工作路径


def log_post():
    logurl = 'https://huaban.com/auth/'
    s.headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Referer': 'http://huaban.com/favorite/beauty/',
        'X-Request': 'JSON',
        'X-Requested-With': 'XMLHttpRequest'

    }
    fromdata = {
        'email': '759885501@qq.com',
        'password': 'qwl1231',
        '_ref': 'fram'
    }

    log_html = s.post(logurl, data=fromdata)  # 发送账号密码登陆，不登陆不能异步加载
    print(log_html.text)
    print('登陆成功    ',log_html.status_code)  # 查看状态码
    # 进入主页爬关注话题图

def strat_maxpage():
    url = 'http://huaban.com/favorite/beauty/'  # 美女话题网址
    wb = s.get(url)  # 模拟Ajax 发送请求获取数据包
    json_data = wb.json()  # 数据包是json 格式，所以用json解析

    for i in json_data.get('pins'):
        id.append(i['pin_id'])
        urllist.append('http://huaban.com/pins/' + str(i['pin_id']))  # 网址具体地址

    return id[-1]


def get_params(maxpage):  # 改变请求头
    params1 = {
        'j7bujbwq': '',
        'max': str(maxpage),
        'limit': '20',
        'wfl': '1'
    }
    return params1

def get_picurl(params1):
    url = 'http://huaban.com/favorite/beauty/'  # 美女话题网址
    wb1 = s.get(url, params=params1)
    json_data1 = wb1.json()

    for i in json_data1.get('pins'):
        id.append(i['pin_id'])
        urllist.append('http://huaban.com/pins/' + str(i['pin_id']))  # 网址具体地址

    return urllist

def down_url(urllist):
    for i in urllist:
        wb2 = s.get(i)  # 获取图片具体网址内容
        json_data2 = wb2.json()
        a = json_data2['pin']['file']['key']
        pic_number.append('http://img.hb.aicdn.com/'+ a )

    return pic_number




if __name__ == '__main__':

    id = []
    urllist = []
    pic_number = []



    s = requests.session()
    log_post()  # 登陆
    maxpage = strat_maxpage()  # 得到最后一个 id

    while True:

        params1 = get_params(maxpage)  # 带入最后一个 pin_id ，得到 ajax params 参数
        urllist = get_picurl(params1)  # 把参数带入 得到 首页图片的具体地址
        maxpage = id[-1]  # 改变最后一个 pin_id
        listpic = down_url(urllist)   # 得到图片下载地址,列表形势存储

        name=dict(map(lambda x,y: [x,y],id,listpic))

        for id,url in name.items():
            pic_jpg = s.get(url)  # 解析具体图片地址
            f = open(str(id) + '.jpg', 'wb')  # 新建文件，以图片id命名
            f.write(pic_jpg.content)  # 二进制写入
            f.close()
            print('正在下载   ' + str(id) + '      地址   ' + url)

        id = []
        urllist = []
        pic_number = []
        print('完成20张， 6 秒后下一组')

        time.sleep(6)
























