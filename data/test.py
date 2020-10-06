import pandas as pd


data = pd.read_csv("card_data.csv")
# for i, r in data.iterrows():
#     if r['id'] == "None":
#         r['id'] = i
#     if r['name'] == "None":
#         r['name'] = ""
#     if r['address'] == "None":
#         r['address'] = ""
#     if r['tel'] == "None":
#         r['tel'] = ""
#     if r['category'] == "None":
#         r['category'] = ""
#     if r['main_mn'] == "None":
#         r['main_mn'] = ""
#     if r['price'] == "None":
#         r['price'] = ""
#     if r['menu'] == "None":
#         r['menu'] = ""
#     if r['opng_tm'] == "None":
#         r['opng_tm'] = ""
#     if r['rating'] == "None":
#         r['rating'] = ""
#     if r['rvw_cnt'] == "None":
#         r['rvw_cnt'] = ""
#     if r['tags'] == "None":
#         r['tags'] = ""
#     if r['img'] == "None":
#         r['img'] = ""

data.to_pickle("card_data.pkl")
# data.to_csv("ent_df2.csv")