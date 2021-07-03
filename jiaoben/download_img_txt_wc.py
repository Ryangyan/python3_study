import requests
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
import urllib3

def download_txt(t_url):
    http=urllib3.PoolManager()
    response = http.request('GET',t_url)
    data = response.data
    txt_str = str(data)
    lines = txt_str.split("\\n")
    des_url = '/Users/yangan/Desktop/test.txt'
    fx = open(des_url,"w")
    for line in lines:
        fx.write(line+ "\n")
    fx.close()

def download_img(img_url, api_token):
    print (img_url)
    header = {"Authorization": "Bearer " + api_token} # 设置http header，视情况加需要的条目，这里的token是用来鉴权的一种方式
    r = requests.get(img_url, headers=header, stream=True)
    print(r.status_code)
    if r.status_code == 200:
        open('/Users/yangan/Desktop/img.jpg','wb').write(r.content) # 将内容写入图片
        print("done")
    del r

if __name__ == '__main__':
    txt_url = "http://textfiles.com/100/gems.txt"
    img_url = "https://img2018.cnblogs.com/blog/1337485/201908/1337485-20190806221849798-407804344.jpg"
    api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    download_img(img_url, api_token)
    download_txt(txt_url)
    text = open(r'/Users/yangan/Desktop/test.txt', "r").read()
    cut_text = jieba.cut(text)
    result = " ".join(cut_text)
    wc = WordCloud(
        background_color='white',
        mask=plt.imread('/Users/yangan/Desktop/img.jpg'),
        max_words=2000,
        max_font_size=80,
        random_state=30
            )
    wc.generate(result)
    wc.to_file(r"/Users/yangan/Desktop/result.png")
    plt.figure("jay")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()