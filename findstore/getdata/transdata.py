import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

from sklearn.preprocessing import LabelEncoder
import re
import time

D_total_df = pd.DataFrame(columns=['id','name','address','tel','category','main_mn','price','opng_tm','break_tm','rating','rvw_cnt','tags','img'])
D_total_review_df = pd.DataFrame(columns=['res_id','res_name','user_name','rating','review'])

data1 = pd.read_csv("../data/MangoPlate3_df.csv")
data2 = pd.read_csv("../data/DiningCode_df.csv")

DiningCode_review_df = pd.read_csv("../data/DiningCode3_review_df.csv")
MangoPlate_review_df = pd.read_csv("../data/MangoPlate3_review_df.csv")
MangoPlate = list(np.array(data1))
DiningCode = list(np.array(data2))
# MangoPlate_review = np.array(MangoPlate_review_df.tolist())
# DiningCode_review = np.array(DiningCode_review_df.tolist())
#기준 : 망고플레이트, 망플이 데이터 더 많음. 망플 ID 기준으로 하자
dic ={}

for mf in MangoPlate:
    key = mf[0]+str(mf[1])
    dic[key] = mf[-1] 
    for dc in DiningCode:
        if mf[0]==dc[0] and mf[1]==dc[1]:
            for i in range(3,12):
                if len(str(mf[i])) <= 3:
                     mf[i] = dc[i]
                     
df = pd.DataFrame(MangoPlate)
df.columns = ['name','address','tel','category','main_mn','price','menu','opng_tm','rating','rvw_cnt','tags','img','id']
df = df[['id','name','address','tel','category','main_mn','price','menu','opng_tm','rating','rvw_cnt','tags','img']]
MangoPlate_review_df = MangoPlate_review_df[['res_id','res_name','user_name','rating','review']]
MangoPlate_review_df['sex'] = 0
MangoPlate_review_df['age'] = 20
MangoPlate_review_df['ppl'] = 2
df=df.astype({'id':'int'})
MangoPlate_review_df = MangoPlate_review_df.sort_values(by=['user_name'], axis=0)
print(df)
print(MangoPlate_review_df)
print(MangoPlate_review_df['user_name'].unique())
# print(MangoPlate)
# print(DiningCode)

#망플에서 없는 데이터는 다이닝코드에서 가져온다.
#리뷰 아이디를 망플 기준으로
#딕셔너리 사용하여 주소+이름을 키로, 벨류를 id로 한 다음 바꾸고 합치자.

# #다이닝코드 id 를 key로 , 망플 id를 value로.
# last_id = len(MangoPlate)
# change_id = {}
# for dc in Diningcode:
#     key = dc[1]+dc[2]
#     if key in dic: #망플에 있다면
#         change_id[dc[0]] = dic.get(key)
#     else: # 망플에 없다면
#         last_id+=1
#         change_id[dc[0]] = last_id
#         dc[0] = last_id
#         MangoPlate.append(dc)


# #다이닝코드 리뷰에서 id를 망플 기준으로 변환
# for dc_r in DiningCode_review:
#     if dc_r[0] in change_id:
#         dc_r[0] = change_id.get(dc_r[0])
#         MangoPlate_review.append(MangoPlate_review_df)


# D_total_review_df = pd.DataFrame(MangoPlate_review)

df.to_pickle('../data/total_df.pkl')
MangoPlate_review_df.to_csv('../data/total_review_df.csv')
