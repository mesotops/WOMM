
# 載入相關套件
#import jieba_fast as jieba  # 切詞
import pandas as pd
import numpy as np


# 讀取運動內衣原始資料
ptt_data = pd.read_csv('PTT_steam_2-4月資料.csv')


# 將重複與空白訊息去除
ptt_data = ptt_data.drop_duplicates()
ptt_data = ptt_data.dropna()


#改時間格式
ptt_data.info()
ptt_data['時間'] = pd.to_datetime(ptt_data['時間'])


#計算留言總數
ptt_data['留言總數']=ptt_data['推推總數']+ptt_data['噓聲總數']+ptt_data['中立總數']


#將分類為【公告】的去除
ptt_data = ptt_data[ptt_data['類別'] != '公告']


# 將「內容」與「所有留言」文字內容合併，創造一欄位 - 「所有文」
ptt_data['所有文'] = ptt_data['標題'] + ptt_data['內容'] 




#去除無意義字元，先進行無意義字元列表，可以自行新增
removeword = ['span','class','f3','https','imgur','h1','_   blank','href','rel','nofollow','target','cdn','cgi','b4','jpg','hl','b1','f5','f4',
            'goo.gl','f2','email','map','f1','f6','__cf___','data','bbs''html','cf','f0','b2','b3','b5','b6','原文內容','原文連結','作者'
            '標題','時間','看板','<','>','，','。','？','—','閒聊','・','/',' ','=','\"','\n','」','「','！','[',']','：','‧','╦','╔','╗','║'
            ,'╠','╬','╬',':','╰','╩','╯','╭','╮','│','╪','─','《','》' ,'.','、','（','）','　','*','※','~','○','”','“','～','@','＋','\r'
            ,'▁',')','(','-','═','?',',','!','…','&',';','『','』','#','＝','＃','\\','\\n', '"', '的', '^', '︿','＠','$','＄','%','％',
            '＆','＊','＿','+',"'",'{','}','｛','｝','|','｜','．','‵','`','；','●','§','※','○','△','▲','◎','☆','★','◇','◆','□','■','▽',
            '▼','㊣','↑','↓','←','→','↖','XD','XDD','QQ','【','】'
            ]

for word in removeword:
    ptt_data['所有文'] = ptt_data['所有文'].str.replace(word,'')


#所有文關鍵字萃取
import jieba as jieba 
jieba.set_dictionary('dict.txt.big')

ptt_data = ptt_data.dropna(subset=["所有文"])
ptt_data['關鍵字'] = ptt_data['所有文'].apply(lambda x: list(jieba.cut(x)))
ptt_data.info()


# 存檔csv
ptt_data.to_csv('PTT_steam_2-4月資料clear.csv',  encoding='UTF-8-sig')


# #留言內容展開
# #第一個貼文留言資料展開   
# comment=ptt_data['留言內容'].iloc[1] #此為str type
# comment1=eval(comment) #此為list type
# new = pd.DataFrame(comment1)
# new
 

#所有貼文留言資料展開                   
newlist = []
for i in range(len(ptt_data)):
    new = pd.DataFrame(eval(ptt_data['留言內容'].iloc[i]))
    newlist.append(new)
        

# 將留言合併成dataframe
ptt_comment = pd.concat(newlist)


#存檔
ptt_comment.to_csv('PTT_steam_2-4月資料留言內容.csv',  encoding='UTF-8-sig')






