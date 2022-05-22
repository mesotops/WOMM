# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:55:36 2019

@author: Ivan
"""

from Ivan_ptt import crawl_ptt_page

## 必要設定的欄位
# 1. 修改ptt板位
# 2. 查看最新的頁數index

steam = crawl_ptt_page(Board_Name ='steam' ,
                            start =3394 ,page_num= 55)


#3. 儲存檔案
steam.to_csv('PTT_steam_2-4月資料.csv',encoding = 'utf-8-sig') 


