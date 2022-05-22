# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:24:45 2019

@author: Ivan
"""

import jieba.analyse
import pandas as pd



# 匯入各電影關鍵字熱度資料
keyword_score = pd.read_csv('allgame_keyword_voice(steam).csv', encoding = 'utf-8')

#資料整理
keyword_score.index = keyword_score['Unnamed: 0']
keyword_score.drop(columns = ['Unnamed: 0'], inplace = True)

#--------------------------------產品知覺圖(全部關鍵字示範)--------------------------------------

for plotX in keyword_score.columns:
    for plotY in keyword_score.columns:
        if plotX == plotY:
            break;
        else:
            # 直接修改上方程式碼貼下來
            x=keyword_score[plotX]
            y=keyword_score[plotY]
            
            # 計算聲量的平均
            Xavg = x.mean()
            Yavg = y.mean()
            
             # 繪製圓點
            import matplotlib.pyplot as plt
            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
            plt.rcParams['axes.unicode_minus'] = False
            colors = ['#ff531a','#f79476','#d9f776','#76d9f7','#9476f7']
            
            plt.figure(figsize=(20,10))
            plt.scatter(x,y, color=colors,s=5000,alpha=0.5)
           
            # 加上文字註解
            for i in range(len(x)):
                plt.text(x[i],y[i], keyword_score.index[i], fontsize=15 )
            
            
            # 畫平均線
            plt.axhline(Yavg, color='c', linestyle='dashed', linewidth=1) # 繪製平均線 
            plt.axvline(Xavg, color='c', linestyle='dashed', linewidth=1) # 繪製平均線    
            
            
            # 標題、X軸標籤、Y軸標籤
            plt.title("GPS市場定位圖 " + plotX + " V.S " + plotY,fontsize=30)#標題
            plt.ylabel(plotY, fontsize=20)#y的標題
            plt.xlabel(plotX, fontsize=20) #x的標題
            plt.show()