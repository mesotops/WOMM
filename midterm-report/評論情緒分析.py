# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:09:46 2021

@author: user
"""

#匯入資料
import pandas as pd
df = pd.read_csv("PTT_steam_2-4月資料留言內容only.csv")


#資料清理
df["ipdatetime"]=pd.to_datetime(df["ipdatetime"])
df.dropna(subset=["content"], inplace=True)


#語句情緒分析
from snownlp import SnowNLP

#一次性處理
df["sentiment"] =  df["content"].apply(lambda x: SnowNLP(x).sentiments)
df.head()


#計算評論情感平均數與中位數
print(df.sentiment.mean())
print(df.sentiment.median())


# #繪圖-每天顯示
# import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
# plt.rcParams['axes.unicode_minus'] = False

# dfselect=df[["ipdatetime","sentiment"]].set_index("ipdatetime").sort_index().head(10)
# dfselect
# dfselect.plot(kind="bar")

# plt.axhline(df.sentiment.mean(), color='c', linestyle='dashed', linewidth=1) 
# plt.xticks(range(len(dfselect.index)), [x.strftime("%Y-%m-%d") for x in dfselect.index], rotation=45)
# plt.show()


#繪圖-按月匯整
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

dfselect1=df[["ipdatetime","sentiment"]].set_index("ipdatetime").resample("M").mean()

dfselect1

dfselect1.plot(kind="bar")
plt.axhline(dfselect1.sentiment.mean(), color='c', linestyle='dashed', linewidth=1) 
plt.xticks(range(len(dfselect1.index)), [x.strftime("%m.%Y") for x in dfselect1.index], rotation=45)
plt.show()


#找出評價最差的一筆
worstreview=df.sort_values(by='sentiment')[:1]["content"].values
#worstreview=df.sort_values(by='sentiment')[:1]["content"]
worstreview





