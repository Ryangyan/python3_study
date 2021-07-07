# -*- coding:utf-8 -*-
"""
作者：ryangyan
日期：2021年07月06日
用途：线程池
"""

import concurrent.futures
import blog_spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)
    htmls = list(zip(blog_spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))
print('craw over')

# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)
        futures[future] = url

    for future, url in futures.items():
        print(url,future.result())