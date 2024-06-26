# -*- coding: utf-8 -*-
"""Text data visualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XyfX9lL1pl39TOKsdTMKYMZce47T9A1U
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

text_data= "We need to take risks"
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text_data)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.title('Word Cloud')
plt.show()
words=text_data.split()
word_counts=Counter(words)
plt.figure(figsize=(10,5))
plt.bar(word_counts.keys(),word_counts.values())
plt.title('Histogram of word frequencies')
plt.xlabel('words')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()