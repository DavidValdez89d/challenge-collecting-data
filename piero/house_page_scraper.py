import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import pandas  as pd


#driver.implicitly_wait(10)

url = 'https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/testelt/3272/9920767'  #Use this link

def get_property(url):
    driver = webdriver.Chrome()
    driver.get(url)

    #Pass the cookkie banner
    time.sleep(2) #its better in a loop
    banner_button = driver.find_element(By.XPATH,'//*[@id="uc-btn-accept-banner"]').click()

    #info = driver.find_element(By.CLASS_NAME,'classified')  #Gets all info in the page
    #info = driver.find_element(By.XPATH,'//head/script[contains(text(),"window.dataLayer")]')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    element_info = soup.select('div.classified script')

    #print(type(element_info))
    text = element_info[0].text

    driver.close()

    #print(text[33:-2])

    return json.loads("".join(("".join(text.split('=')[1:]).split(";")[:-1])))

#start = time.time()

#house_dictionary = dict()
url_list = ['https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/testelt/3272/9920767','https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/averbode/3271/10120498','https://www.immoweb.be/en/classified/new-real-estate-project-houses/for-sale/berlaar/2590/10130433']
#for url in url_list:
#    house_dictionary[url]=get_property(url)
#
#print(house_dictionary.keys())
#
#end = time.time()
#
#print("the time is:", end-start)
#
def main(url_list):
    ##urls = get_page_link(url)
    houses_list = [product_data(url) for url in url_list]
    #df = pd.DataFrame(houses_list)
    #df = df.rename(index = lambda x: x + 1)
    #print(df.describe())
    #df.to_csv("properties.csv")
    df = pd.DataFrame(houses_list[0])
    df = df.rename(index = lambda x: x + 1)
    for i in range(len(houses_list)-1):
        df2 = pd.DataFrame(houses_list[i+1])
        df.append(df2, ignore_index = False)
        df = df.rename(index = lambda x: x + 1)
        print(df.describe())
        df.to_csv(f"properties{i}.csv")
main(url_list)
#data_open_fire = 0
#data_terrace = 0
#data_garden = 0
#data_surface_of_the_land = 0
#data_surface_of_the_plot_of_land = 0
#data_number_of_facades = 0
#data_swimming_pool = 0
#data_state_of_the_building = 0

#print('\n--------------\ninfo',info.text)