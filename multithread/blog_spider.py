# -*- coding:utf-8 -*-
"""
作者：ryangyan
日期：2021年07月06日
用途：
"""
import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/sitehome/p/{page}"
    for page in range(1, 50 + 1)
]


def craw(url):
    r = requests.get(url)
    return r.text


def parse(html):
    # class ="post-item-title"
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[2])):
        print(result)
