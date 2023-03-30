# -*- coding=utf-8 -*-
# @Time: 2023/3/30 16:40
# @AUTHOR: HUI
# @File: word.py
# @software: PyCharm
import jieba
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
txt = "人生不留遗憾，但遗憾也就遗憾吧,宁愿多坚持一秒，也不后悔一辈子。我们真的很累，想在梦想的路上放弃，但是当我们放弃的时候，我们将一无所有，所以我们不能放弃。因为我们别无选择，只能勇往直前。珍惜缘分，珍惜感情。茫茫人海能遇见，是难得的缘分"
pic = Image.open("pk.jpg")  # 打开图片路径，形成轮廓
shape = np.array(pic)  # 图像轮廓转换为数组
words = jieba.cut(txt)
nextxt = ' '.join(words)
wordcloud = WordCloud(mask=shape,font_path="msyh.ttf",background_color='white',width=200,height=200).generate(nextxt).to_file("demo1.jpg")
plt.imshow(wordcloud)
plt.axis("off")
plt.show()