import pandas as pd
import matplotlib.pyplot as plt


books = pd.read_csv('/Users/yangan/Desktop/books.csv',encoding='utf-8')
print("————————————————打印行索引————————————————")
print(books.index)
print("————————————————打印列索引————————————————")
print(books.columns)
print("————————————————平均评分最大值———————————————")
print(max(books['average_rating']))
print("————————————————算出每年出版数的数量———————————————")
yearlist=[]
intlist=[]
for i in books['original_publication_year']:
    if pd.isnull(i):# 空值跳过
        continue
    else:
        if i not in yearlist:
            yearlist.append(int(i))
            temp=len(books.loc[books['original_publication_year']==i])
            intlist.append(temp)
            # print('在%s年出版了%d本书'%(i,temp))
print("————————————————降序排序———————————————")
mydict=dict(zip(yearlist,intlist))
a = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
x=[]
y=[]
for i in a:
    x.append(str(i[0])+'年')
    y.append(i[1])
    print('在%d年出版了%d本书'%(i[0],i[1]))

plt.bar(x[:10],y[:10])
plt.yticks(range(0,601,50),size = 10)
plt.title('不同出版年份书的数量（前10名）')
plt.savefig('/Users/yangan/Desktop/result_bar.png', dpi=300) #指定分辨率保存