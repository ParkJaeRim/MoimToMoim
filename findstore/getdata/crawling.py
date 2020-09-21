import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

import re
import time

# D_restaurants_df = pd.DataFrame(columns=['id','name','address','category','main_mn','price','menu','opng_tm','rating','rvw_cnt','tags','img'])
# D_review_df = pd.DataFrame(columns=['res_id','res_name','user_name','rating','review'])

# with open("../data/restaurants_DiningCode2.txt","r") as f:
#     text = f.read()
#     urls = text.split()
# def crawling_reviews_DiningCode(name, link,id):
#     reviews = pd.DataFrame(columns=['res_id','res_name','user_name','rating','review'])
#     try:
#         driver.get(link)
#     except:
#         return None
#     while True:
#         try:
#             click_more = driver.find_element_by_xpath("""//*[@id="div_more_review"]""")
#             click_more.click()
#         except:
#             break
            
#     time.sleep(1)
    
#     try:
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'html.parser')
        
#         for user in soup.find('div',{'id':'div_review'}).find_all('div',{'id':re.compile('div_review_+')}):
#             tmp = user.find('span','btxt').get_text()
#             user_name = tmp[:tmp.find('(')].strip()
#             user_rating = int(re.findall('\d+',user.find('i',{'style':re.compile('width:+')})['style'])[0])//20
#             user_review = user.find('p','review_contents btxt').get_text().replace('\n','')
        
#             reviews = reviews.append({'res_id':id,
#                                     'res_name':name,
#                                     'user_name':user_name,
#                                     'rating':user_rating,
#                                     'review':user_review}, ignore_index=True)
#     except:
#         return None
    
#     driver.close()
    
#     return reviews
# def crawling_res_data_DiningCode(link,id):
    
#     #링크 불러오기
#     try:
#         html = urlopen(link)
#         html.encoding = 'utf-8'
#         soup = BeautifulSoup(html, "html.parser")
#     except:
#         print('링크 에러:', link)
#         return None,None,None,None,None,None,None,None,None,None
    
#     #상호명
#     try:
#         name=soup.find_all('p','tit')[3].get_text()
#         print(name)
#     except:
#         name=None
    
#     #주소
#     try:
#         address = soup.find('li','locat').get_text()
#     except:
#         address = None
    
#     #업종(다이닝코드엔 업종이 없음)
#     category = None
    
#     #주메뉴
#     try:
#         main_menu = soup.find('div','menu-info short').find_all('p','l-txt')[0].get_text().strip()
#     except:
#         main_menu = None
    
#     #가격(주메뉴)
#     try:
#         price = int(soup.find('div','menu-info short').find_all('p','r-txt')[0].get_text()[:-1].replace(',',''))
#     except:
#         price = None
    
#     #메뉴
#     try:
#         menu = ''
#         for menus in soup.find('ul','Restaurant_MenuList').find_all('li'):
#             menu += menus.find('span','Restaurant_Menu').get_text()
#             menu += ':'
#             menu += menus.find('span','Restaurant_MenuPrice').get_text()
#             menu += '//'
#         menu=menu[:-1]

#     except:
#         menu = None

    
#     #영업시간
#     try:
#         time_dict = dict()
#         opening_time_list = soup.find('div','busi-hours short').find_all('p')[1:]
#         for i in range(len(opening_time_list))[0::2]:
#             if opening_time_list[i].get_text()!='더보기':
#                 time_dict[opening_time_list[i].get_text()] = opening_time_list[i+1].get_text()
    
#         opening_time = str(time_dict)
#     except:
#         opening_time = None
    
#     #평점과 리뷰 수
#     try:
#         ratings = float(soup.find('strong','rate-point').span.get_text())
#         tmp = ratings[0].get_text().strip()
#         rating = float(ratings[1].get_text()[:-1])
#         review_count = tmp[:tmp.find('명')]
#     except:
#         rating = None
#         review_count = None                 
    
#     #태그
#     try:
#         tags = ','.join([i.get_text()[:i.get_text().find('(')] for i in soup.find_all('p','icon')])
#     except:
#         tags = None
    
#     #이미지 :망플에서 들고 올거임
#     img =None
#     res_reviews = crawling_reviews_DiningCode(name, url,id)
    

#     return name, address, category, main_menu, price, menu, opening_time, rating, review_count, tags,img, res_reviews


# count = 1
# for url in urls:
#     driver = webdriver.Chrome('driver/chromedriver')

#     print(count,'\t|',end='')
    
#     name, address, category, main_menu, price, menu, opening_time, rating, review_count, tags, img, review_df = crawling_res_data_DiningCode(url,count)    
#     D_restaurants_df = D_restaurants_df.append({'id':count,
#                                             'name':name,
#                                             'address':address,
#                                             'category':category,
#                                             'main_mn':main_menu,
#                                             'price':price,
#                                             'menu':menu,
#                                             'opng_tm':opening_time,
#                                             'rating':rating,
#                                             'rvw_cnt':review_count,
#                                             'tags':tags,
#                                             'img':img}, ignore_index=True)

#     D_review_df = D_review_df.append(review_df, ignore_index=True)

#     count+=1
# D_restaurants_df.to_csv('../data/DiningCode3_df.csv',index=False)
# D_review_df.to_csv('../data/DiningCode3_review_df.csv', index=False)

M_restaurants_df = pd.DataFrame(columns=['name','address','tel','category','main_mn','price','menu','opng_tm','rating','rvw_cnt','tags','img'])
M_review_df = pd.DataFrame(columns=['res_name','user_name','rating','review'])


with open("../data/restaurants_MangoPlate2.txt","r") as f:
    text = f.read()
    Mango_urls = text.split()

print(len(Mango_urls))


### 상점 데이터 크롤링
def crawling_res_data_MangoPlate(link,id):
    driver.get(link)
    #링크 불러오기
    try:
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    except:
        print('Link Error:', link)
        return None,None,None,None,None,None,None,None,None,None,None,None,None,None
    
    #상호명
    try:
        name= soup.find('h1','restaurant_name').get_text()
        print(name)
    except:
        name=None
    
    #주소
    try:
        address = soup.find('div','Restaurant__InfoAddress--Text').get_text()
    except:
        address = None
    
    #전화번호
    try:
        tel = soup.select('tbody > tr')[1].td.get_text()
    except:
        tel = None

    #업종
    try:
        category = soup.select('tbody > tr')[2].span.get_text()
    except:
        category = None
    
    #주메뉴
    try:
        main_menu = soup.find_all('span','Restaurant_Menu')[0].get_text()
    except:
        main_menu = None
    
    #가격(주메뉴)
    try:
        price = int(soup.find_all('span','Restaurant_MenuPrice')[0].get_text()[:-1].replace(',',''))
    except:
        price = None
    
    #메뉴
    try:
        menu = ''
        for menus in soup.find('ul','Restaurant_MenuList').find_all('li'):
            menu += menus.find('span','Restaurant_Menu').get_text()
            menu += ':'
            menu += menus.find('span','Restaurant_MenuPrice').get_text()
            menu += '//'
        menu=menu[:-1]

    except:
        menu = None

    #영업시간
    try:
        opening_time = soup.select('tbody > tr')[5].td.get_text()
    except:
        opening_time = None
    

    #평점 
    try:
        rating = float(soup.find('strong','rate-point').span.get_text())
    except:
        rating = None
        
    #리뷰 수
    try:
        review_count = int(soup.find('span','cnt review').get_text())
    except:
        review_count = None                 
    

    tags = None

    try:
        img = str(soup.find("img","center-croping").get("src").split("?")[0])
        # print(img)
    except:
        img=None
    
    res_reviews = crawling_reviews_MangoPlate(name, link, id)
    
    return id, name, address, tel, category, main_menu, price, menu, opening_time,rating, review_count, tags, img, res_reviews


def crawling_reviews_MangoPlate(name, link,id):
    reviews = pd.DataFrame(columns=['res_id','res_name','user_name','rating','review'])
    more_count = 0
    while (more_count<=20):
        try:
            time.sleep(1)
            driver.find_element_by_xpath("""/html/body/main/article/div[1]/div[1]/div/section[3]/div[2]""").click()
            more_count+=1
        except:
            break

    tabs = driver.window_handles
    
    if len(tabs)>=2:
        for i in range(len(tabs))[:0:-1]:
            driver.switch_to.window(tabs[i])
            driver.close()

    driver.switch_to.window(tabs[0])
    
    try:
        time.sleep(0.5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        users = soup.find_all('a','RestaurantReviewItem__Link')

        rating_score = {'맛있다':5,'괜찮다':3,'별로':1}

        for user in users:
            user_name = user.span.get_text()
            user_review = user.p.get_text().strip()
            user_rating = user.find('span','RestaurantReviewItem__RatingText').get_text()
            user_rating = rating_score[user_rating]
            
            reviews = reviews.append({
                                    'res_id':id,
                                    'res_name':name,
                                    'user_name':user_name,
                                    'rating':user_rating,
                                    'review':user_review}, ignore_index=True)        
    except:
        return None
    
    
    return reviews


count = 1
driver = webdriver.Chrome('driver/chromedriver')

for url in Mango_urls:

    print(count,'\t|',end='')
    
    id, name, address, tel, category, main_menu, price, menu, opening_time, rating, review_count, tags,img, review_df = crawling_res_data_MangoPlate(url,count)    
    M_restaurants_df = M_restaurants_df.append({'id':id,
                                            'name':name,
                                            'address':address,
                                            'category':category,
                                            'tel': tel,
                                            'main_mn':main_menu,
                                            'price':price,
                                            'menu':menu,
                                            'opng_tm':opening_time,
                                            'rating':rating,
                                            'rvw_cnt':review_count,
                                            'tags':tags,
                                            'img':img}, ignore_index=True)
    M_review_df = M_review_df.append(review_df, ignore_index=True)

    count+=1

M_restaurants_df.to_csv('../data/MangoPlate3_df.csv',index=False)
M_review_df.to_csv('./MangoPlate3_review_df.csv', index=False)