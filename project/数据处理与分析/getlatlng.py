import pandas
from bs4 import BeautifulSoup 
from urllib import request
import re
import pandas as pd
import numpy as np
import urllib.parse as urp
from xml.etree import ElementTree
import time

#获取某地经纬度
def __get_location1__(name,city):  
        my_ak = 'wwG6oij98cQBnT48PkjQdErOKT6SjKSg'    # 填写申请的百度AK
        #tag = urp.quote('地铁站')
        qurey = urp.quote(name)
        try:
            url = 'http://api.map.baidu.com/place/v2/search?query='+qurey+'&tag='+'&region='+urp.quote(city)+'&output=json&ak='+my_ak
            #print(url)
            req = request.urlopen(url)
            res = req.read().decode()
            lat = pd.to_numeric(re.findall('"lat":(.*)',res)[0].split(',')[0])
            lng = pd.to_numeric(re.findall('"lng":(.*)',res)[0])
            return (lng,lat)  #经度和纬度
        except:
            return 0,0

#在原始数据上，新增经度和维度列
df = pd.read_csv(r'数据处理与分析\rent_final.csv', header= 0,names =['title','location','price','url','source','lng','lat'])

for i in range(len(df)):
    if df.loc[i,'lng'] == 0.0:
        lng,lat = __get_location1__(str(df.loc[i,'location']),'北京')
        print(lng,lat,i,df.loc[i,'location'])
        df.loc[i,'lng'] = lng
        df.loc[i,'lat'] = lat

df.to_csv('rent_final.csv',index = 0)