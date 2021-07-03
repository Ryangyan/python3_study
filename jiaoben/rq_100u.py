from lxml import etree
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By
from queue import Queue
from selenium import webdriver
from threading import Thread
import os

class Biquge():
    def __init__(self,base_url):
        self.base_url = base_url
        self.driver = webdriver.PhantomJS()
        #30隐性等待时间，如果30秒，目标位置还没加载完成就取消执行
        self.wait = WebDriverWait(self.driver,30)
        self.get_article_num()

    def get_etree_by_xpath(self,url,xpath):
        self.driver.get(url)
        target = self.wait.until(ES.presence_of_element_located((By.XPATH,xpath)))
        html = self.driver.page_source
        html_tree = etree.HTML(html)
        return html_tree
        # 根据文章的类型创建文件夹

    def create_dir_write(self,text=None,article_type=None,filename=None,l=[]):
        #只要不重新赋值给l l的值会保存不会变化
        # 如果有类型l为空
        if article_type:
            l.append(article_type)
        # 如果文件夹存在直接写入
        if os.path.exists('./article/%s' % (l[-1])):
            # 写入文件文件名
            with open('./article/%s/%s.txt' % (l[-1], filename), 'a+', encoding='utf-8') as h:
                h.write(text)
                # os.mkdir('./article/%s/%s' %(l[0],filename))
        else:
            # 先创建类型的目录
            os.makedirs('./article/%s' % (article_type))

    def get_list_one(self, lst):
        if lst:
            return lst[0].strip()
        return ''

    #获取每章的内容
    def article_zhang_detail(self,article_zhang_name,article_zhang_url,article_name):
        article_detail_etree = self.get_etree_by_xpath(article_zhang_url,'//div[@id="content"]')
        article_detail_list = ['\n','\n',article_zhang_name,'\n','\n'] + article_detail_etree.xpath('//div[@id="content"]/text()')
        for article_detail in article_detail_list:
            self.create_dir_write(text=article_detail,filename=article_name)


    def article_list(self,article_li):
        article_name = self.get_list_one(article_li.xpath('.//a/text()'))
        article_url = self.get_list_one(article_li.xpath('.//a/@href'))
        print(article_name, article_url)
        #获取小说的章节目录
        article_list_etree = self.get_etree_by_xpath(article_url, '//div[@id="list"]')
        #获取章节list
        article_dd_list = article_list_etree.xpath('//div[@id="list"]/dl/dd')
        for article_dd_zhang in article_dd_list:
            article_zhang_url = 'http://www.xbiquge.la' + self.get_list_one(article_dd_zhang.xpath('.//a/@href'))
            article_zhang_name = self.get_list_one(article_dd_zhang.xpath('.//a/text()'))
            print(article_zhang_name,article_zhang_url)
            self.article_zhang_detail(article_zhang_name,article_zhang_url,article_name)

    #获取所有小说的种类
    def get_article_num(self):
        #获取小说种类
        etree_home = self.get_etree_by_xpath(self.base_url,'//div[@id="main"]')
        for n in range(1,7):
            article_type = self.get_list_one(etree_home.xpath('//div[@id="main"]/div[%s]/h2/text()'%n))
            article_li_list = etree_home.xpath('//div[@id="main"]/div[%s]/ul/li'%n)
            print(article_type)
            self.create_dir_write(article_type=article_type)
            for article_li in article_li_list:
                self.article_list(article_li)



if __name__ == '__main__':
    base_url = 'http://www.xbiquge.la/xiaoshuodaquan/'
    b = Biquge(base_url)

