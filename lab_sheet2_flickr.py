# -*- coding: utf-8 -*-
"""lab_sheet2 flickr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1isijEl82leFH1OO5WJbZcmb1OtXE14kj
"""

import pandas as pd
import numpy as np
from functools import reduce

df=pd.read_csv("/content/BL-Flickr-Images-Book.csv")
df.head(25)

df.shape

to_drop=["Edition Statement","Corporate Author","Engraver","Former owner"]

df.drop(to_drop,inplace=True,axis=1)
df.head()

for col in df.columns:
  print(col)

df.set_index('Identifier',inplace=True)
df.head()

unwanted_characters=['[',',','_']

def clean_dates(item):
  dop=str(item['Date of Publication'])
  if dop=='nan'or dop[0]=='[':
    return np.NaN
  for character in unwanted_characters:
    if character in dop:
       character_index=dop.find(character)
       dop=dop[:character_index]
  return dop
df['Date of Publication']=df.apply(clean_dates,axis=1)

df['Date of Publication'].head(25)

def clean_title(title):
  if title=='nan':
    return 'NaN'
  if title[0]=='[':
    title=title[1:title.find(']')]
  if 'by'in title:
    title =title[:title.find('by')]
  elif 'By'in title:
      title=title[:title.find('By')]
  if'[' in title:
    title=title[:title.find('[')]
    title=title[:-2]
    df['title']=df['title'].apply(clean_title)
    df.head()

df.loc[4159587]
df.head(25)