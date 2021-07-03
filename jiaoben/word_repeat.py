#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:03:36 2020

@author: yangan
"""


# Str = input('输入密码：')
# print('原码为：',end='')
# for i in range(0, len(Str)):
#     if Str[i] == ' ':
#         print(' ', end="")
#     else:
#         print(chr(ord(Str[i])-3),end='')

# wl=input('请输入武力值：')
# sd=input('请输入速度值：')
# zl=input('请输入智力值：')
# tz=input('请输入统治值：')
# print("武力是 {0:5}".format(wl)+"*"*(int(wl)//10))
# print("速度是 {0:5}".format(sd)+"*"*(int(sd)//10))
# print("智力是 {0:5}".format(zl)+"*"*(int(zl)//10))
# print("统治是 {0:5}".format(tz)+"*"*(int(tz)//10))

# for i in range(13):
#     if i==0 or i==6 or i==12:
#         print('+',end='')
#         for j in range(5):
#             print('- ',end='')
#         print('+',end='')
#         for j in range(5):
#             print('- ',end='')
#         print('+')
#     else:
#         print('1',end='')
#         for j in range(5):
#             print('  ',end='')
#         print('1',end='')
#         for j in range(5):
#             print('  ',end='')
#         print('1')

#e6.6RedDreamofMansions.py
# import jieba
# txt = open("/Users/yangan/Desktop/红楼梦.txt","r",encoding='utf-8').read()
# words = jieba.lcut(txt)
# excludes=['什么','一个','我们','那里','如今','你们','说道','知道','起来','姑娘','这里','出来','他们','众人','奶奶','自己','一面'
#           ,'只见','怎么','两个','没有','不是','不知','听见','这个','这样','进来','咱们','就是','东西','告诉','回来','只是','大家',
#           '只得','这些','不敢','出去','所以','不过','不好','的话','一时','过来','不能','心里','今日','姐姐','太太','丫头','银子',
#           '如此','二人','几个','答应','这么','还有','只管','一回','说话','那边','外头','这话','打发','自然','罢了','今儿','屋里']
# counts = {}
# for word in words:
#       if len(word) == 1:
#             continue
#       else:
#             counts[word] = counts.get(word,0) + 1
# for word in excludes:
#       del(counts[word])
# items = list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(5):
#       word,count = items[i]
#       print("{0:<10}{1:>5}".format(word,count))



# import string
 
# def get_dict_word_times(file):
#     list_word_with_punctuation = file.read().split()
#     # 去掉标点，不区分大小写
#     list_word = [word.strip(string.punctuation).lower() for word in list_word_with_punctuation]
#     # 去掉重复单词
#     set_word = set(list_word)
#     return {word: list_word.count(word) for word in set_word}
 
 
# def main():
#     # 战争与和平第一章
#     with open('/Users/yangan/Desktop/WarandPeace.txt', 'r') as file:
#         dict_word_times = get_dict_word_times(file)
#     # 把单词按照次数由多到少排序
#     list_sorted_words = sorted(dict_word_times, key=lambda w: dict_word_times[w], reverse=True)
#     for i in range(8):
#         word=list_sorted_words[i]
#         print("{} -- {} times".format(word, dict_word_times[word]))
 
# main()
url=('10000000', '00001011', '00000011', '00011111')
print("%d.%d.%d.%d"%(int(url[0],2),int(url[1],2),int(url[2],2),int(url[3],2)))


