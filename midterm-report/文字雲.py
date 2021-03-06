#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:22:00 2019

@author: cheating
"""
#------------文字雲------------
from PIL import Image # 圖片轉array陣列
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator #文字雲
from collections import Counter
import pandas as pd

# 匯入原始爬蟲資料
steamGame=pd.read_csv("PTT_steam_2-4月資料clear.csv")

# 將重複與空白訊息去除
steamGame.drop_duplicates()
steamGame.dropna(inplace=True)


#資料欄位整合，所有文字變成一個大字串
theSTR=str(steamGame["所有文"].sum())


#-------------資料清理，無意義字元去除-------------
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
              'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
              'goo.gl','f2','email','map','f1','f6','__cf___','steamGame','bbs'
              'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
              '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',
              ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
              ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
              ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
              ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
              ,'\l']

for i in removeword:
    theSTR=theSTR.replace(i,"")
    
#用正規表達式去除數字
import re
re.sub(r'\d',"",theSTR)

#用正規表達式去除所有無意義字元
re.sub(r'(\d)|(\[])',"",theSTR)

#範例，尋找字串中有網址的並取代
pattern='[a-zA-z]+://[^\s]*'
re.sub(pattern,"",theSTR)

import jieba 
jieba.set_dictionary('dict.txt.big')
jieba.load_userdict('user_dict.txt')

words=jieba.lcut(theSTR, cut_all=False)

match = ['ELDEN RING','elden ring','法環','艾爾登']
for i in range(len(words)):
    for j in match:
        if words[i] == j:
            words[i]= "艾爾登法環"

match = ['鬼線東京','幽靈線','鬼線','Ghostwire: Tokyo']
for i in range(len(words)):
    for j in match:
        if words[i] == j:
            words[i]= "鬼線:東京"

match = ['消逝的光芒2','消逝的光芒2 人與仁之戰','消逝的光芒','人與仁之戰','Dying Light 2 Stay Human','垂死之光']
for i in range(len(words)):
    for j in match:
        if words[i] == j:
            words[i]= "垂死之光2"
            
match = ['師傅','sifu','Sifu','SIFU']
for i in range(len(words)):
    for j in match:
        if words[i] == j:
            words[i]= "師父"
            
match = ['魔物獵人','怪獵','崛起','MONSTER HUNTER','rise','Rise','RISE','MONSTER HUNTER RISE','MHR','米飯']
for i in range(len(words)):
    for j in match:
        if words[i] == j:
            words[i]= "魔物獵人:rise"

#中文繪圖需要中文字體，設定字型，微軟正黑體
font = r'msjh.ttc'
my_wordcloud = WordCloud(font_path=font,collocations=False, width=2400, height=2400, margin=2)  

#生成文字雲
my_wordcloud.generate_from_frequencies(frequencies=Counter(theSTR))

#顯示文字雲
plt.imshow(my_wordcloud)
plt.axis("off") #取消座標



