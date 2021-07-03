import requests
from bs4 import BeautifulSoup
import pandas as pd
import re





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
    colleges_list=soup.find_all('tr',class_={'bgfd','bgf5'})
    for college in colleges_list:
        chidern=college.find_all('td')
        c_id=chidern[0].string
        c_name=chidern[1].find('a').string
        temp=re.findall('[a-z，A-Z]{2,}\.png',str(chidern[2]))
        c_country=str(temp[0])[:-4]
        if pd.isnull(chidern[3].string):
            c_score=chidern[3].string
        else:
            c_score=float(chidern[3].string)
        ilt.append([c_id,c_name,c_score,c_country])
    return ilt

        
def saveData(ilt):
    columns_list=['排名','学校名称','综合分数','国家或地区']
    df=pd.DataFrame(ilt,columns=columns_list)
    df.to_csv('/Users/yangan/Desktop/foreigncollege.csv',index=False,\
              encoding='utf_8_sig')

def main():

    info=[]
    try:
        html=getHTML(url)
        praseHTML(info,html)
    except:
        print("请求错误")
    saveData(info)
    
url='http://www.zuihaodaxue.cn/FieldSCI2016.html'
main()













