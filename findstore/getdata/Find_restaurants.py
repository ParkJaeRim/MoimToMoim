from selenium import webdriver
import time
#서울시 구 정의 : 총 24개의 구
# gu_list = ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구",
#           "노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성북구",
#            "송파구","양천구","영등포구","용산구","은평구","종로구","중구", "중랑구"]
gu_list = ["강남구","성동구","마포구"]

#다이닝 코드에서 식당 링크 가져오기
def get_links_DiningCode(gu):
    driver = webdriver.Chrome('driver/chromedriver')
    driver.get("https://www.diningcode.com/list.php?query=서울%20"+gu)
    
    while True:
        try:
            click_more = driver.find_element_by_xpath("""//*[@id="div_list_more"]""")
            click_more.click()
        except:
            break
        time.sleep(0.5)
        
    link_list = driver.find_elements_by_tag_name("a")
    res_links_raw = [link.get_attribute('href') for link in link_list]
    res_links = []
    for link in res_links_raw:
        if link.find('profile')!=-1:
            res_links.append(link)
            
    res_links = list(set(res_links))
    Diningcode_links.extend(res_links)
    print('Found',len(res_links),'places from '+gu)
    
    # If get not enough data
    if len(res_links) < 80 :
        retry.append(gu)
    
    driver.close()

Diningcode_links = []
retry = []
for gu in gu_list:
    get_links_DiningCode(gu)
for gu in retry:
    get_links_DiningCode(gu)


Diningcode_links = list(set(Diningcode_links))

# save into text
with open("../data/restaurants_DiningCode2.txt","w") as f:
    f.write('\n'.join(Diningcode_links))

#망고플레이트에서 식당 링크 가져오기
def get_links_MangoPlate(gu):    
    try:
        driver.get("https://www.mangoplate.com/search/서울%20"+gu)
    except:
        return

    count = 0
    res_links = []
    
    for i in range(1,11):
        try:
            click_more = driver.find_element_by_xpath("""/html/body/main/article/div[2]/div/div/section/div[4]/p/a["""+str(i)+"""]""")
            click_more.click()
            time.sleep(0.5)
        
            link_list = driver.find_elements_by_tag_name("a")
            res_links_raw = [link.get_attribute('href') for link in link_list]
            res_links_raw = list(set(res_links_raw))
        except:
            continue
        
        
        for link in res_links_raw:
            if link.find('restaurants')!=-1:
                res_links.append(link)

    res_links = list(set(res_links))            
    MangoPlate_links.extend(res_links)
    print('Found',len(res_links),'places from '+gu)
    
    # If get not enough data
    if len(res_links) < 80 :
        retry.append(gu)

    
driver = webdriver.Chrome('driver/chromedriver')
MangoPlate_links = []
retry = []
driver.get("https://www.mangoplate.com/search/서울%20강남구")

for gu in gu_list:
    get_links_MangoPlate(gu)
for gu in retry:
    get_links_MangoPlate(gu)

get_links_MangoPlate('성북구')
driver.close()

MangoPlate_links = list(set(MangoPlate_links))
len(MangoPlate_links)
# save into text
with open("../data/restaurants_MangoPlate2.txt","w") as f:
    f.write('\n'.join(MangoPlate_links))