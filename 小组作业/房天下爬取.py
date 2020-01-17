import requests
import os
from pyquery import PyQuery as pq
import csv
import pandas as pd
import re

area=["chaoyang","haidian","fengtai","xicheng","dongcheng","changping","daxing","tongzhou","fangshan","shunyi","shijingshan","miyun","mentougou","huairou","yanqing","pinggu"]
area_pages={'chaoyang':3,'haidian':2,'fengtai':2,'xicheng':1,'dongcheng':1,'changping':3,'daxing':4,'tongzhou':3,'fangshan':2,'shunyi':3,'shijingshan':1,'miyun':1,'mentougou':1,'huairou':1,'yanqing':1,'pinggu':1}


def getmessage(i,x):
    y=1
    title=[]
    price=[]
    address=[]
    while (y<=x):
        url='https://newhouse.fang.com/house/s/{area}/b9{pages}/?ctm=1.bj.xf_search.page.2'.format(area=area[i],pages=y)
        r = requests.get(url) #获取该页面
        r.encoding = 'GBK'
        html = r.text #获取代码信息
        doc = pq(html)#获取内容
        
        
        p0=doc("[class='nhouse_price']")#爬取价格

        ps=doc("[class='kanesf']")#找到掉售完的楼房
        ps.parent().children().remove()#去掉售完的楼房的所有子节点

        t0=doc("[class='nlcd_name'] a")#爬取标题
        a0=doc("[class='address'] a")#爬取地址
        a0.find('span').remove()#整理地址
        where=doc('title')#爬取地区标题

        t1=t0.text()
        p1=p0.text()
        a1=a0.text()
        w1=where.text()

        t2=t1.split()
        p2=p1.split()
        a2=a1.split()

        title.extend(t2)
        price.extend(p2)
        address.extend(a2)

        y=y+1

        return title,price,address,w1


if __name__=='__main__':
    for i in range(0,16):
        x=area_pages[area[i]]
        title=[]
        price=[]
        address=[]
        (title,price,address,w1)=getmessage(i,x)
        dataframe = pd.concat([pd.DataFrame({'标题':title}),pd.DataFrame({'价格':price}),pd.DataFrame({'地址':address})],axis=1)
        dataframe.to_csv(w1+".csv",index=False,sep=',',encoding="utf_8_sig")
    
