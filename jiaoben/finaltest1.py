from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
text="""There is always a moment when I want to collapse. I imagine that when I was a teenager, 
I would have a big cry in advance or a hysterical roar, but I finally realized that the collapse was silent, 
trying to brew for half a day and finding that a tear could not be squeezed out. The adult world would be short of balance without efforts and tears"""
cut_text = jieba.cut(text)
result = " ".join(cut_text)
wc = WordCloud(
        background_color='white',
        max_words=2000,
        max_font_size=50,
        random_state=30
            )
wc.generate(result)
wc.to_file(r"/Users/yangan/Desktop/result_wc.png")
plt.figure("jay")
plt.imshow(wc)
plt.axis("off")
plt.show()