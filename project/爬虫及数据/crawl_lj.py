from bs4 import BeautifulSoup
import requests
import csv
import time
import re
import random

csv_file = open('rent_lj.csv','w',newline='',encoding='utf-8')
writer = csv.writer(csv_file, delimiter=',')

browser = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
]

page = 1
headers = {
    'Origin': 'https://bj.lianjia.com',
    'Referer': 'https://bj.lianjia.com/ditiezufang/pg2/',
    'User-Agent': random.choice(browser)
}

while page<= 100:
    url = 'https://bj.lianjia.com/ditiezufang/pg' + str(page) + '/#contentList'
    print(page,url)
    time.sleep(2)
    res = requests.get(url,headers =headers)
    print(res.status_code)
    html = res.text
    soup = BeautifulSoup(html,'html.parser')

    items = soup.find_all('div',class_='content__list--item--main')
    for item in items:
        title = item.find('p',class_='content__list--item--title twoline').find('a').text.lstrip()
        title2 = item.find('p',class_= 'content__list--item--des').find_all('a')[1].text
        title3 = title2 + ' ' + title
        if '青年公寓' in title:
            continue
        add = re.findall('.*?·(.*?) .*',title)[0]
        price = item.find('em').text
        link = 'https://bj.lianjia.com' + item.find('p',class_='content__list--item--title twoline').find('a')['href']
        writer.writerow([title3.lstrip(),add,price,link])
    page += 1

csv_file.close()  
