import requests
import os
from bs4 import BeautifulSoup

url = 'http://www.mzitu.com/all/'
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}


wb_data=requests.get(url,headers=headers)
soup=BeautifulSoup(wb_data.text,'lxml')

img=soup.find('div',class_="all").find_all('a')
os.mkdir(r'/Users/langlanglang/Downloads/mzitu/')

for i in img:
    title=i.get_text()
    path = r'/Users/langlanglang/Downloads/mzitu/' + title
    os.mkdir(path)
    os.chdir(path)

    pic_link=i.get('href')
    html_pic=requests.get(pic_link,headers=headers)
    soup_pic=BeautifulSoup(html_pic.text,'lxml')
    max_page=soup_pic.find('div',class_='pagenavi').find_all('span')[-2].get_text()

    for number in range(1,int(max_page)+1):
        url_pic=pic_link+'/' + str(number)

        end_data_pic=requests.get(url_pic,headers=headers)
        end_soup=BeautifulSoup(end_data_pic.text,'lxml')
        end_img=end_soup.find('div',class_='main-image').find('img')['src']
        name=end_img[-9:]
        headers2={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36','Referer':end_img}
        pic_jpg=requests.get(end_img,headers=headers2)

        print('正在下载:'+ title + name)

        f=open(name,'ab')
        f.write(pic_jpg.content)
        f.close()











