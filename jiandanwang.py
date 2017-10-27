import requests
import urllib.request
import time
from os import mkdir
from bs4 import BeautifulSoup

urls = ['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(256,290)]
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

n=0
def pic_download(url):
    time.sleep(2)
    global n
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    img=soup.select('div > div > div.text > p > img')
    folder_path=r'/Users/langlanglang/Downloads/pic/'
    for i in img:
        pic_link=('http:'+i.get('src'))
        n=n+1
        urllib.request.urlretrieve(pic_link, folder_path + '\\' + str(n) + pic_link[-4:])
        print('Download',pic_link)

    print('=============  next page ===========')


for i in urls:
    pic_download(i)