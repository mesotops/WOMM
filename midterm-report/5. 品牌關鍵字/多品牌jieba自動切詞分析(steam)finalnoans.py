# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import jieba 
import matplotlib.pyplot as plt
import jieba.analyse
import re

# 匯入原始爬蟲資料
steamGame=pd.read_csv("PTT_steam_2-4月資料clear.csv")

# 將重複與空白訊息去除
steamGame.drop_duplicates()
steamGame.dropna(inplace=True)

steamGame['所有文'] = steamGame['所有文'].str.replace('ELDEN RING','艾爾登法環')
steamGame['所有文'] = steamGame['所有文'].str.replace('elden ring','艾爾登法環')
steamGame['所有文'] = steamGame['所有文'].str.replace('法環','艾爾登法環')
steamGame['所有文'] = steamGame['所有文'].str.replace('艾爾登','艾爾登法環')

steamGame['所有文'] = steamGame['所有文'].str.replace('鬼線東京','鬼線:東京')
steamGame['所有文'] = steamGame['所有文'].str.replace('幽靈線','鬼線:東京')
steamGame['所有文'] = steamGame['所有文'].str.replace('鬼線','鬼線:東京')
steamGame['所有文'] = steamGame['所有文'].str.replace('Ghostwire: Tokyo','鬼線:東京')

steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒2','垂死之光2')
steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒2 人與仁之戰','垂死之光2')
steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒','垂死之光2')
steamGame['所有文'] = steamGame['所有文'].str.replace('人與仁之戰','垂死之光2')
steamGame['所有文'] = steamGame['所有文'].str.replace('Dying Light 2 Stay Human','垂死之光2')
steamGame['所有文'] = steamGame['所有文'].str.replace('垂死之光','垂死之光2')

steamGame['所有文'] = steamGame['所有文'].str.replace('師傅','師父')
steamGame['所有文'] = steamGame['所有文'].str.replace('sifu','師父')
steamGame['所有文'] = steamGame['所有文'].str.replace('Sifu','師父')
steamGame['所有文'] = steamGame['所有文'].str.replace('SIFU','師父')

steamGame['所有文'] = steamGame['所有文'].str.replace('魔物獵人','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('怪獵','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('崛起','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('MONSTER HUNTER','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('rise','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('Rise','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('RISE','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('MONSTER HUNTER RISE','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('MHR','魔物獵人:rise')
steamGame['所有文'] = steamGame['所有文'].str.replace('米飯','魔物獵人:rise')

list=['艾爾登法環','鬼線:東京','垂死之光2','師父','魔物獵人:rise']
for x in list:
    #下條件找出符合條件的資料，再資料欄位整合，所有文字變成一個大字串
    steamGame_slected=steamGame[steamGame["所有文"].str.contains(x)]
    theSTR=str(steamGame_slected["所有文"].sum())
    
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
    re.sub(r'\d',"",theSTR)
    
    #用正規表達式去除所有無意義字元
    re.sub(r'(\d)|(\[])',"",theSTR)
    
    #範例，尋找字串中有網址的並取代
    pattern='[a-zA-z]+://[^\s]*'
    re.sub(pattern,"",theSTR)
    
    
    # #品牌名字統一
    # match = ['ELDEN RING','elden ring','法環','艾爾登']
    # for i in match:
    #     theSTR=theSTR.replace(i,"艾爾登法環")
    
    # match = ['鬼線東京','幽靈線','鬼線','Ghostwire: Tokyo']
    # for i in match:
    #     theSTR=theSTR.replace(i,"鬼線:東京")
        
    # match = ['消逝的光芒2','消逝的光芒2 人與仁之戰','消逝的光芒','人與仁之戰','Dying Light 2 Stay Human','垂死之光']
    # for i in match:
    #     theSTR=theSTR.replace(i,"垂死之光2")
        
    # match = ['師傅','sifu','Sifu','SIFU']
    # for i in match:
    #     theSTR=theSTR.replace(i,"師父")
    
    # match = ['魔物獵人','怪獵','崛起','MONSTER HUNTER','rise','Rise','RISE','MONSTER HUNTER RISE','MHR','米飯']
    # for i in match:
    #     theSTR=theSTR.replace(i,"魔物獵人:rise")
        
    # match = ['bug','BUG']
    # for i in match:
    #     theSTR=theSTR.replace(i,"Bug")    
    
    # match = ['dlc','Dlc']
    # for i in match:
    #     theSTR=theSTR.replace(i,"DLC")    
        
    
    #-------------Jieba將字串斷詞，變成list-------------

    keywords_top=jieba.analyse.extract_tags(theSTR ,topK=5, withWeight=True) #基于TF-IDF算法進行關鍵詞抽取
    
    keywords_top_DF = pd.DataFrame(keywords_top,columns=["字詞","聲量"])
    
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    #繪圖
    plt.bar(keywords_top_DF["字詞"], keywords_top_DF["聲量"]) #給予線標籤
    plt.xlabel('關鍵字',fontsize=15)
    plt.ylabel('熱度',fontsize=15)
    plt.title(x+'關鍵字排名',fontsize=20)
    plt.show()