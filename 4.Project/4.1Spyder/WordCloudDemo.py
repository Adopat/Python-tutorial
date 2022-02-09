# 词云Demo
import jieba, numpy
from PIL import Image
from wordcloud import WordCloud
import collections

with open('ylxb.txt', 'r', encoding='utf-8') as f:
    words = f.read()
new_words = ' '.join(jieba.cut(words))
word_counts = collections.Counter(new_words)  # 统计切词后，每个词出现的次数
print('前10词:', word_counts.most_common(15))
alice_mask = numpy.array(Image.open('gaogenxie.jpg'))
wordcloud = WordCloud(width=100,
                      height=860,
                      margin=2,
                      mask=alice_mask,
                      background_color='#d4ff80',  # 设置背景颜色
                      font_path=r'C:\Windows\Fonts\STSONG.TTF')
wordcloud.generate(new_words)
wordcloud.to_file('ylxb3.jpg')
