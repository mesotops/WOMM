#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:22:00 2019

@author: cheating
"""
import pandas as pd
import numpy as np


#讀入聲量資料
allgm_voice=pd.read_csv('game_voice_df.csv')
allgm_voice.drop(columns="Unnamed: 0", inplace=True)


# 讀入情緒資料
game_NLP=pd.read_csv('allgame_sensation_score(steam).csv') #開啟檔案
game_NLP.drop(columns="Unnamed: 0", inplace=True)


#各電影電影名稱、聲量、情緒分數變list
game =allgm_voice["遊戲名稱"].tolist()
mv_voice=allgm_voice["聲量"].tolist()
mv_emotion=game_NLP["sensation_score"].tolist()


    
#-----------------------繪圖------------------------------------
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False


#繪製象限圖，判斷四個象限所在的位置，來決定顏色
plt.figure(figsize=(20,10))

axe_list = []
for i in range(len(mv_emotion)):
    if mv_emotion[i]>np.mean(mv_emotion) and mv_voice[i] >np.mean(mv_voice):#第一象限
        color = '#66b877' 
        axe = '第一象限'
        
    elif mv_emotion[i]>np.mean(mv_emotion) and mv_voice[i] <= np.mean(mv_voice):#第四象限
        color = '#66a7b8'
        axe = '第四象限'
        
    elif mv_emotion[i]<=np.mean(mv_emotion) and mv_voice[i] > np.mean(mv_voice):#第二象限
        color = '#b866a7'
        axe = '第二象限'
        
    else:#第二象限
        color = '#b87766'
        axe = '第三象限'
    
    # 繪製圓點
    plt.scatter(mv_emotion[i],mv_voice[i], color=color,s=100*mv_voice[i],alpha=0.5)
    #plt.scatter(mv_emotion[i],mv_voice[i], color=color,alpha=0.5)
    #plt.scatter(mv_emotion[i],mv_voice[i], color=color,s=5000,alpha=0.5)
    
    # 加上文字註解
    plt.text(mv_emotion[i],mv_voice[i], game[i], fontsize=15 )
    
    #儲存象限資料
    axe_list.append(axe)
    

    
plt.axhline(np.mean(mv_voice), color='c', linestyle='dashed', linewidth=1) # 繪製平均線 
plt.axvline(np.mean(mv_emotion), color='c', linestyle='dashed', linewidth=1) # 繪製平均線    

plt.title("聲量 V.S 情緒",fontsize=30)#標題
plt.ylabel("聲量",fontsize=20)#y的標題
plt.xlabel("情緒（0～1）",fontsize=20) #x的標題
plt.ylim(0,max(allgm_voice["聲量"]+20))
plt.show()


#將聲量情緒象限資料儲存起來
axe_list_df=pd.DataFrame(axe_list) #list轉換為df
allgm_VEA_df=pd.concat([allgm_voice, game_NLP, axe_list_df],axis=1)  #合併聲量、情緒、象限
# allgm_VEA_df.drop(columns=["遊戲名稱"],inplace=True) #去除多餘欄位
allgm_VEA_df.rename(columns={0:"象限"}, inplace=True) #改欄位名
allgm_VEA_df.to_csv("聲量情緒.csv",encoding='UTF-8-sig')


#繪製長條與折線
fig, ax1 = plt.subplots()

plt.title('聲量情緒圖')
plt.xlabel('遊戲名稱')
plt.xticks(rotation=90)
ax2 = ax1.twinx()

#ax1
ax1.bar(allgm_VEA_df["遊戲名稱"],allgm_VEA_df["聲量"])
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.set_ylabel('遊戲聲量',color='tab:blue')
#ax1.axhline(np.mean(mv_voice), color='tab:blue', linestyle='dashed', linewidth=1) # 繪製平均線

#ax2
ax2.plot(allgm_VEA_df["遊戲名稱"],allgm_VEA_df["sensation_score"],alpha=0.5,color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylabel('情緒',color='black')
#ax2.axhline(np.mean(mv_emotion), color='black', linestyle='dashed', linewidth=1) # 繪製平均線  

fig.tight_layout()
plt.show()
fig.tight_layout()
plt.show()