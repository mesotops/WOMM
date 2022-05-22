
import pandas as pd

steamGame=pd.read_csv('PTT_steam_2-4月資料留言內容.csv')
feature = ['劇情','支線','成就','攻略','難','Bug','優化','任務','挑戰','DLC']

steamGame.dropna(subset=['content'], inplace=True)
steamGame['content'] = steamGame['content'].str.replace('ELDEN RING','艾爾登法環')
steamGame['content'] = steamGame['content'].str.replace('elden ring','艾爾登法環')
steamGame['content'] = steamGame['content'].str.replace('法環','艾爾登法環')
steamGame['content'] = steamGame['content'].str.replace('艾爾登','艾爾登法環')

steamGame['content'] = steamGame['content'].str.replace('鬼線東京','鬼線:東京')
steamGame['content'] = steamGame['content'].str.replace('幽靈線','鬼線:東京')
steamGame['content'] = steamGame['content'].str.replace('鬼線','鬼線:東京')
steamGame['content'] = steamGame['content'].str.replace('Ghostwire: Tokyo','鬼線:東京')

steamGame['content'] = steamGame['content'].str.replace('消逝的光芒2','垂死之光2')
steamGame['content'] = steamGame['content'].str.replace('消逝的光芒2 人與仁之戰','垂死之光2')
steamGame['content'] = steamGame['content'].str.replace('消逝的光芒','垂死之光2')
steamGame['content'] = steamGame['content'].str.replace('人與仁之戰','垂死之光2')
steamGame['content'] = steamGame['content'].str.replace('Dying Light 2 Stay Human','垂死之光2')
steamGame['content'] = steamGame['content'].str.replace('垂死之光','垂死之光2')

steamGame['content'] = steamGame['content'].str.replace('師傅','師父')
steamGame['content'] = steamGame['content'].str.replace('sifu','師父')
steamGame['content'] = steamGame['content'].str.replace('Sifu','師父')
steamGame['content'] = steamGame['content'].str.replace('SIFU','師父')

steamGame['content'] = steamGame['content'].str.replace('魔物獵人','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('怪獵','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('崛起','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('MONSTER HUNTER','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('rise','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('Rise','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('RISE','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('MONSTER HUNTER RISE','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('MHR','魔物獵人:rise')
steamGame['content'] = steamGame['content'].str.replace('米飯','魔物獵人:rise')

steamGame['content'] = steamGame['content'].str.replace('bug','Bug')
steamGame['content'] = steamGame['content'].str.replace('BUG','Bug')

steamGame['content'] = steamGame['content'].str.replace('dlc','DLC')
steamGame['content'] = steamGame['content'].str.replace('Dlc','DLC')

# 產出每一個Tag欄位，計算每一個商品被該Tag提到與否
for i in feature:
    steamGame[i] = steamGame['content'].apply(lambda x: 1 if i in x else 0) # 如果留言內容含feature字詞，就計數１
   

#根據每個使用者做彙總
steamGame["聲量"]=1

feature.append("聲量") #將聲量欄位名加入特徵值list，以利後續讀取資料使用

steamGame_cluster= steamGame.groupby(['user'], as_index=False) [feature].sum()


# 將'user','聲量'設定爲index，這樣做分群的時候就不會被當特徵值
steamGame_cluster = steamGame_cluster.set_index(['user', '聲量'])


# --------------機器學習自動決定要分多少群

# ####方法一Elbow，找轉折點
from sklearn.cluster import KMeans

distortions = []
for k in range(1,15):
    kmeanModel = KMeans(n_clusters=k,random_state=1).fit(steamGame_cluster)
    distortions.append(kmeanModel.inertia_) #Inertia計算群內所有點到該群的中心的距離的總和。


import matplotlib.pyplot as plt

plt.figure(figsize=(16,8))
plt.plot(range(1,15), distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

#-------------------最後決定分6群------------------------
clustering = KMeans(n_clusters=6,random_state=1).fit(steamGame_cluster)


clustering.labels_ #查看分群標籤
clustering.cluster_centers_ #查看各群中心值

# 將群放入steamGame_cluster
steamGame_cluster['群'] = clustering.labels_


# 將之前的user', '聲量'解放回來
steamGame_cluster = steamGame_cluster.reset_index()


# 設定過渡參數【人數】，後續用來統計每一群的市場人數
steamGame_cluster['人數'] = 1

# 找出每一個群體的特徵加總
steamGame_cluster_group= steamGame_cluster.groupby(['群'], as_index=False).sum()
steamGame_cluster_group.to_csv("steamGame_cluster_group.csv",encoding='UTF-8-sig')

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

steamGame_cluster_group.drop(columns=['聲量','人數'], inplace=True)
steamGame_cluster_group.set_index('群', inplace=True)
steamGame_cluster_group.plot()
plt.title('各群關鍵字')
plt.xlabel('群類別')
plt.ylabel('關鍵詞聲量')
plt.xticks(range(len(steamGame_cluster_group.index)), steamGame_cluster_group.index)
plt.show()

print('Done!')


