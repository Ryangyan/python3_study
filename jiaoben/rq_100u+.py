#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:57:00 2020

@author: yangan
"""


import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import csv

url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "404 Found" # just for fun

def praseHTML(ilt,html):
#解析HTML文本
    soup=BeautifulSoup(html,'html.parser')
    print(soup.title)
    colleges_list=soup.find_all('tr',class_='alt')
    for college in colleges_list:
        chidern=college.find_all('td')
        c_id=chidern[0].string
        c_name=chidern[1].find('div').string
        c_location=chidern[2].string
        c_type=chidern[3].string
        c_score=chidern[4].string
        c_score1=chidern[5].string
        c_score2=chidern[6].string
        c_score3=chidern[7].string
        c_score4=chidern[8].string
        c_score5=chidern[9].string
        c_score6=chidern[10].string
        c_score7=chidern[11].string
        c_score8=chidern[12].string
        c_score9=chidern[13].string
        c_score10=chidern[14].string
        ilt.append([c_id,c_name,c_location,c_type,c_score,\
                    c_score1,c_score2,c_score3,c_score4,\
                        c_score5,c_score6,c_score7,c_score8,\
                            c_score9,c_score10])
    return ilt

def printData(ilt):
    tplt='{:4}\t{:30}\t{:10}\t{:8}\t{:4}'
    print(tplt.format('排名','学校名称','地点','类型','综合分数'))
    for c in ilt:
        print(tplt.format(c[0],c[1],c[2],c[3],c[4]))
        
def saveData(ilt):
    columns_list=['排名','学校名称','地点','类型','综合分数','办学层次',\
                  '学科水平','办学资源','师资规模与结构','人才培养','科学研究',\
                      '服务社会','高端人才','重大项目与成果','国际竞争力']
    df=pd.DataFrame(ilt[:100],columns=columns_list)
    df.to_csv('/Users/yangan/Desktop/college.csv',index=False,\
              encoding='utf_8_sig')

def main():

    info=[]
    try:
        html=getHTML(url)
        praseHTML(info,html)
    except:
        print("请求错误")
    printData(info)
    saveData(info)
    

main()











