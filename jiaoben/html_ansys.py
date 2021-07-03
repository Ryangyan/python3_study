#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:52:16 2020

@author: yangan
"""

import urllib.request
import re
from bs4 import BeautifulSoup

html="""
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
 Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
 and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
 and they lived at the bottom of a well.
</p>
<p class="story">...</p>
</body>
</html>
"""
soup=BeautifulSoup(html,"lxml")
print("----------a标签的全部属性----------")
print(soup.a.attrs)
print("----------a标签的指定属性----------")
print(soup.a.attrs['href'])
print(soup.a.attrs['class'])
print(soup.a.string)
print("----------bs库标签名找标签a----------")
print(soup.find_all(name='a'))
print("----------bs库属性名找标签p----------")
print(soup.find_all(attrs={"class":"story"}))
print("----------正则表达式找标签a----------")
html_temp=html.replace('\n', '')
pattern=re.compile('<a(.+?)</a>')
result=pattern.findall(html_temp)
print(result)

print(re.findall('abc*','abcabcccab'))
print(re.findall('abc+','abcabcccab'))
print(re.findall('abc?','abcabcccab'))
print(re.findall('abc{2}','abcabcccab'))
print(re.findall('abc{2,}','abcabcccab'))


# mystr="10000000 00001011 00000011 00011111"

# def ip2to10(string):
#     templist=string.split(' ')
#     result=''
#     for i in range(4):
#         result+=str(int(templist[i],2))+'.'
#     return result[:-1]


# url=
# data={}
# data.

# r = urllib.request.urlopen(url,data)
# cat_img = r.read()
# with open('/Users/yangan/Desktop/cat.jpg','wb') as f:
#     f.write(cat_img)
#     f.close()

# string="I love 123 FishC.com"
# print(re.search("\d\d\d\.\d\d\d\.\d\d\d\.", string))