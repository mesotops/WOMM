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

steamGame['所有文'] = steamGame['所有文'].str.replace('bug','Bug')
steamGame['所有文'] = steamGame['所有文'].str.replace('BUG','Bug')

steamGame['所有文'] = steamGame['所有文'].str.replace('dlc','DLC')
steamGame['所有文'] = steamGame['所有文'].str.replace('Dlc','DLC')

list=['艾爾登法環','鬼線:東京','垂死之光2','師父','魔物獵人:rise']
brand_keyword_voice=[]
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
                  ,'.',',','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
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
        
    
    #-------------Jieba將字串斷詞，變成list-------------
    jieba.set_dictionary('dict.txt.big')
    jieba.load_userdict('user_dict.txt')
    words=jieba.lcut(theSTR, cut_all=False)
            
    #-------------自訂關鍵字計算-------------
    
    #關鍵字列表
    focus_keyword=['劇情','支線','成就','攻略','難','Bug','優化','任務','挑戰','DLC']
    
    #關鍵字在jieba斷詞字串出現的次數
    focus_keyword_voice=[]
    for j in focus_keyword:
        focus_keyword_voice.append(words.count(j))
    
    print(focus_keyword_voice)
    brand_keyword_voice.append(focus_keyword_voice)
    print(brand_keyword_voice)
        
    #關鍵字跟熱度結合
    focus_keyword_df=pd.DataFrame(zip(focus_keyword,focus_keyword_voice))
    focus_keyword_df.columns=["關鍵字","熱度"]
        
    ### 把keywords畫成棒狀圖
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    
    
    plt.bar(focus_keyword_df["關鍵字"], focus_keyword_df["熱度"]) 
    plt.xlabel('關鍵字',fontsize=15)
    plt.ylabel('熱度',fontsize=15)
    plt.title(x +'關鍵字排名',fontsize=20)
    plt.show() 
    
allbrand_keyword_voice = pd.DataFrame(brand_keyword_voice , columns=(focus_keyword) , index=list)
allbrand_keyword_voice.to_csv("allgame_keyword_voice(steam).csv",encoding='UTF-8-sig')

allbrand_keyword_voice.plot(figsize=(10,5),title="各品牌各關鍵字熱度圖")
plt.xlabel('brand',fontsize=15)
plt.ylabel('關鍵字熱度',fontsize=15)
plt.xticks(range(len(allbrand_keyword_voice.index)),allbrand_keyword_voice.index,fontsize=10,rotation=90)
plt.savefig('各品牌各關鍵字熱度圖.png')
plt.show()