import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import re

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 匯入原始爬蟲資料
steamGame=pd.read_csv('PTT_steam_2-4月資料clear.csv') #開啟檔案

# 將重複與空白訊息去除
steamGame.drop_duplicates()
steamGame.dropna(inplace=True)

#-----------去除無意義字元
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel',
              'nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
              'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs'
              'html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
              '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',
              ' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
              ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》','_'
              ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
              ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝'
              ,'\l']

#迴圈逐字取代
for i in removeword:
    steamGame["所有文"] = steamGame["所有文"].apply(lambda x: x.replace(i,""))

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
sensation_score=[]
for i in list:

    #下條件找出符合條件的資料
    steamGame_slectedtemp=steamGame[steamGame["所有文"].str.contains(i)]   
    steamGame_slected=steamGame_slectedtemp.copy() #複製一份複本。如果沒有此行，也是可以執行，只是會出現warning訊息  
    
    #------------------計算情緒分數。以一大段文字為單位，去計算情緒
    #各列資料計算情緒分數
    steamGame_slected["sentiment"] =  steamGame_slected["所有文"].apply(lambda x: SnowNLP(x).sentiments)
    
    #計算評論情感平均數
    steamGame_slected.sentiment.mean()
    sensation_score.append(steamGame_slected.sentiment.mean())
    print(sensation_score)
    
#繪圖
# steamGame_slected["sentiment"].plot(kind="bar")
# plt.xticks(range(len(steamGame_slected)), steamGame_slected["時間"], rotation=45)
# plt.show()
    
allsensation_score = pd.DataFrame(sensation_score,columns =['sensation_score'] , index= list)
allsensation_score.to_csv("allgame_sensation_score(steam).csv",encoding='UTF-8-sig')

allsensation_score.plot(figsize=(10,5),title="各遊戲情緒得分")
plt.xlabel('game',fontsize=15)
plt.ylabel('sensation_score',fontsize=15)
plt.xticks(range(len(allsensation_score.index)),allsensation_score.index,fontsize=10,rotation=90)
plt.show()
