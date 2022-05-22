# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:23:45 2021

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt

# 匯入原始爬蟲資料
steamGame=pd.read_csv("PTT_steam_2-4月資料clear.csv")

# 將重複與空白訊息去除
steamGame.drop_duplicates()
steamGame.dropna(inplace=True)

#品牌名字統一
# steamGame['所有文'] = steamGame['所有文'].str.replace('ELDEN RING','艾爾登法環')
# steamGame['所有文'] = steamGame['所有文'].str.replace('elden ring','艾爾登法環')
# steamGame['所有文'] = steamGame['所有文'].str.replace('法環','艾爾登法環')
# steamGame['所有文'] = steamGame['所有文'].str.replace('艾爾登','艾爾登法環')

# steamGame['所有文'] = steamGame['所有文'].str.replace('鬼線東京','鬼線:東京')
# steamGame['所有文'] = steamGame['所有文'].str.replace('幽靈線','鬼線:東京')
# steamGame['所有文'] = steamGame['所有文'].str.replace('鬼線','鬼線:東京')
# steamGame['所有文'] = steamGame['所有文'].str.replace('Ghostwire: Tokyo','鬼線:東京')

# steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒2','垂死之光2')
# steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒2 人與仁之戰','垂死之光2')
# steamGame['所有文'] = steamGame['所有文'].str.replace('消逝的光芒','垂死之光2')
# steamGame['所有文'] = steamGame['所有文'].str.replace('人與仁之戰','垂死之光2')
# steamGame['所有文'] = steamGame['所有文'].str.replace('Dying Light 2 Stay Human','垂死之光2')
# steamGame['所有文'] = steamGame['所有文'].str.replace('垂死之光','垂死之光2')

# steamGame['所有文'] = steamGame['所有文'].str.replace('師傅','師父')
# steamGame['所有文'] = steamGame['所有文'].str.replace('sifu','師父')
# steamGame['所有文'] = steamGame['所有文'].str.replace('Sifu','師父')
# steamGame['所有文'] = steamGame['所有文'].str.replace('SIFU','師父')

# steamGame['所有文'] = steamGame['所有文'].str.replace('魔物獵人','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('怪獵','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('崛起','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('MONSTER HUNTER','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('rise','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('Rise','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('RISE','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('MONSTER HUNTER RISE','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('MHR','魔物獵人:rise')
# steamGame['所有文'] = steamGame['所有文'].str.replace('米飯','魔物獵人:rise')

#資料欄位整合，所有文字變成一個大字串
steamGame["所有文"]=steamGame["標題"]+steamGame["內容"]
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

#-------------Jieba將字串斷詞，變成list-------------
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
            

#-------------多品牌聲量計算-------------

game = ['艾爾登法環','鬼線:東京','垂死之光2','師父','魔物獵人:rise']

game_voice=[]
for m in game:
    voice=words.count(m)
    game_voice.append(voice)

game_voice_df=pd.DataFrame(zip(game,game_voice))       
game_voice_df.columns=["遊戲名稱","聲量"]


#顯示品牌聲量繪圖
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.bar(game_voice_df["遊戲名稱"],game_voice_df["聲量"])
plt.xlabel("遊戲名稱")
plt.ylabel("聲量")
plt.title('各遊戲聲量',fontsize=20)
plt.xticks(rotation=90)
plt.axhline(game_voice_df["聲量"].mean(), linestyle="dashed")
plt.show()


game_voice_df.to_csv("game_voice_df.csv",encoding='UTF-8-sig')


